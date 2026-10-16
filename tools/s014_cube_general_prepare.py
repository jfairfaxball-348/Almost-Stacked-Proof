import hashlib,itertools,json,random
from pathlib import Path
B=Path('evidence/S014/cube_general');B.mkdir(exist_ok=True);S=Path('evidence/S014/cube_dag');L=Path('evidence/S014/cube_lower');assert json.loads((S/'verification_v2.json').read_bytes())['complete_AS_tail_upper31'] and json.loads((L/'verification.json').read_bytes())['exact_binary_buffer_AS_oracle_certified'];rng=random.Random(14060);cases=[];seen=set();sign=[(-1)**v.bit_count() for v in range(16)]
def canonical(c):
    s=min(v for v in range(16) if c[v]==max(c));return tuple(c[v^s] for v in range(16))
def add(c,family):
    c=canonical(c)
    if c in seen:return
    seen.add(c);cases.append(dict(id=len(cases),c=c,mass=sum(c),family=family))
for v in range(16):c=[2]*16;c[v]-=1;add(c,'all2_minus1')
add([2]*16,'all2')
for v in range(16):c=[2]*16;c[v]+=1;add(c,'all2_plus1')
H={0,3,5,6}
for M in [31,32,33]:
    for U in itertools.combinations([v for v in range(16) if v not in H],M-28):
        c=[7*int(v in H)+int(v in U) for v in range(16)]
        if sum(a*b for a,b in zip(c,sign))%3==0:add(c,'four7_structured')
uniform={};paired={}
for M in [31,32,33]:
    rows=[];local=set()
    while len(rows)<2048:
        bars=[-1]+sorted(rng.sample(range(M+15),15))+[M+15];c=[bars[i+1]-bars[i]-1 for i in range(16)];c=canonical(c)
        if c in local or sum(z>=2 for z in c)<2 or sum(z>0 for z in c)<4 or sum(a*b for a,b in zip(c,sign))%3:continue
        local.add(c);rows.append(c)
    uniform[M]=rows;rows=[];local=set()
    while len(rows)<1024:
        t=rng.choice([1,3,7,15]);off=[v for v in range(16) if v not in [0,t]];bits=rng.randrange(1<<14);c=[0]*16
        for i,v in enumerate(off):c[v]=int(bits>>i&1)
        remainder=M-sum(c);a=rng.randrange(2,remainder-1);c[0]=a;c[t]=remainder-a;c=canonical(c)
        if c in local or sum(z>0 for z in c)<4 or sum(a*b for a,b in zip(c,sign))%3:continue
        local.add(c);rows.append(c)
    paired[M]=rows
for i in range(2048):
    for M in [31,32,33]:
        add(uniform[M][i],'uniform_signed0')
        if i<1024:add(paired[M][i],'twoheavy_signed0')
assert len(cases)<=9799 and all(c['mass'] in [31,32,33] and sum(z>=2 for z in c['c'])>=2 for c in cases);cfg=json.loads((S/'inputs.json').read_bytes());cfg['candidates']=cases;(B/'inputs.json').write_text(json.dumps(cfg,separators=(',',':'))+'\n',encoding='utf-8',newline='\n');plan=Path('sessions/S014/PLAN_AMENDMENT_60.md');plan.with_suffix('.sha256').write_text(hashlib.sha256(plan.read_bytes()).hexdigest()+'\n',encoding='ascii',newline='\n');files=[plan,plan.with_suffix('.sha256'),B/'inputs.json',S/'nodes.bin.xz',S/'choices.json',S/'verification_v2.json',S/'repair_preflight.json',L/'verification.json',L/'preflight.json',Path('tools/s014_cube_lower.py'),Path('research/S014_BINARY_BUFFER_LOWER_ANNOTATIONS.md'),Path('research/S014_BINARY_BUFFER_UPPER_CERTIFICATES.md'),Path('tools/s009_checks.py'),*Path('tools').glob('s014_cube_general*.py')]
(B/'preflight.json').write_text(json.dumps(dict(files={p.as_posix():hashlib.sha256(p.read_bytes()).hexdigest() for p in files}),indent=2)+'\n',encoding='utf-8',newline='\n');print('CAM60 frozen',len(cases),'actual non-AS inputs; exact Q4 L_AS30')
