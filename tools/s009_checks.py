"""Read-only cold/final check runner, timeout/resource logs retained in S009."""
import ctypes
import hashlib
import json
import subprocess
import sys
import time
from ctypes import wintypes
from pathlib import Path

class Memory(ctypes.Structure):
    _fields_=[('cb',wintypes.DWORD),('faults',wintypes.DWORD),('peak',ctypes.c_size_t),('working',ctypes.c_size_t),
        ('peak_pool',ctypes.c_size_t),('pool',ctypes.c_size_t),('peak_nonpool',ctypes.c_size_t),('nonpool',ctypes.c_size_t),
        ('pagefile',ctypes.c_size_t),('peak_pagefile',ctypes.c_size_t)]

def run(cmd,timeout=600):
    start=time.monotonic();p=subprocess.Popen(cmd,stdout=subprocess.PIPE,stderr=subprocess.PIPE)
    peak=0;failure=None
    if sys.platform=='win32':
        kernel=ctypes.WinDLL('kernel32',use_last_error=True)
        kernel.OpenProcess.restype=wintypes.HANDLE
        handle=kernel.OpenProcess(0x0400|0x0010,False,p.pid)
    else: handle=None
    while p.poll() is None:
        if handle:
            counters=Memory();counters.cb=ctypes.sizeof(counters)
            ctypes.windll.psapi.GetProcessMemoryInfo(handle,ctypes.byref(counters),counters.cb)
            peak=max(peak,counters.peak)
        if time.monotonic()-start>timeout: failure='TIME_CUTOFF';p.kill();break
        if peak>2*1024**3: failure='MEMORY_CUTOFF';p.kill();break
        time.sleep(.1)
    if handle: kernel.CloseHandle(handle)
    out,err=p.communicate()
    return {'command':cmd,'exit_code':p.returncode,'seconds':time.monotonic()-start,'peak_working_set_bytes':peak,
        'resource_failure':failure,'stdout':out.decode('utf-8',errors='replace'),'stderr':err.decode('utf-8',errors='replace'),
        'code_sha256':hashlib.sha256(Path(cmd[1]).read_bytes()).hexdigest() if len(cmd)>1 and Path(cmd[1]).is_file() else None}

def main():
    cold=['s004_cold','s004_structure','s004_witness_tests','s005_pure','s005_check_traces',
          's006_verify','s006_stack_verify','s006_challenges','s006_extrema','s006_obstruction_verify',
          's007_tail_verify','s007_tail_verify --stack','s008_tip_verify','s008_symbolic','s008_branches_verify']
    checks=[ [sys.executable,'tools/'+s.split()[0]+'.py','--check-only']+s.split()[1:] for s in cold ]
    dest=Path('evidence/S009/cold_checks.json');rows=[]
    for cmd in checks:
        row=run(cmd);rows.append(row)
        dest.write_text(json.dumps(rows,indent=2)+'\n',encoding='utf-8',newline='\n')
        print(json.dumps({k:v for k,v in row.items() if k in ('command','exit_code','seconds','peak_working_set_bytes','resource_failure')}),flush=True)
        if row['exit_code']!=0: print(row['stderr'],flush=True);sys.exit(1)

if __name__=='__main__':main()
