"""Bounded read-only final governance run; output logged separately then manifested."""
import ctypes,hashlib,json,os,subprocess,sys,tempfile,time
from pathlib import Path
from s009_checks import Memory

dest=Path('evidence/S014/closeout_validation.json')
assert not dest.exists(), 'Preserve previous attempt before retrying'
cmd=[sys.executable,'validation/validate_governance.py'];start=time.monotonic();peak=0;failure=None
# Administrative rehash only: no mathematical campaign bounds are changed.
# File-backed streams cannot deadlock on an undrained pipe during supervision.
with tempfile.TemporaryFile() as out,tempfile.TemporaryFile() as err:
 env=os.environ.copy();env['PYTHONUNBUFFERED']='1'
 p=subprocess.Popen(cmd,stdout=out,stderr=err,env=env)
 if sys.platform=='win32':
  kernel=ctypes.WinDLL('kernel32',use_last_error=True);kernel.OpenProcess.restype=ctypes.wintypes.HANDLE
  handle=kernel.OpenProcess(0x0400|0x0010,False,p.pid)
 else:handle=None
 while p.poll() is None:
  if handle:
   m=Memory();m.cb=ctypes.sizeof(m);ctypes.windll.psapi.GetProcessMemoryInfo(handle,ctypes.byref(m),m.cb);peak=max(peak,m.peak)
  if peak>2*1024**3:failure='MEMORY_CUTOFF';p.kill();break
  if time.monotonic()-start>1800:failure='TIME_CUTOFF';p.kill();break
  time.sleep(.1)
 p.wait()
 if handle:kernel.CloseHandle(handle)
 out.seek(0);err.seek(0)
 row=dict(command=cmd,exit_code=p.returncode,seconds=time.monotonic()-start,peak_working_set_bytes=peak,resource_failure=failure,stdout=out.read().decode('utf-8',errors='replace'),stderr=err.read().decode('utf-8',errors='replace'),code_sha256=hashlib.sha256(Path(cmd[1]).read_bytes()).hexdigest(),scope='Administrative complete historical/S014 provenance validation, 1800s/2GiB; no new search or change to any mathematical run bound; file-backed unbuffered stdout/stderr.')
dest.write_text(json.dumps(row,indent=2)+'\n',encoding='utf-8',newline='\n')
print(json.dumps(row),flush=True)
if row['exit_code'] or row['resource_failure']:raise SystemExit(1)
