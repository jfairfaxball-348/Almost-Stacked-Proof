from pathlib import Path
def save(name,t):Path('tools/'+name+'.py').write_text(t,encoding='utf-8',newline='\n')
for name in ['cegis','verify','potential','lrat_verify']:
    t=Path('tools/s014_lex_'+name+'.py').read_text(encoding='utf-8').replace('evidence/S014/lex_cegis','evidence/S014/split_cegis').replace('evidence/S014/lex_lrat','evidence/S014/split_lrat')
    save('s014_split_'+name,t)
t=Path('tools/s014_lex_run.py').read_text(encoding='utf-8').replace('evidence/S014/lex_cegis','evidence/S014/split_cegis').replace('evidence/S014/lex_lrat','evidence/S014/split_lrat').replace('s014_lex_','s014_split_')
a="shard=int(sys.argv[1]);assert shard in [0,1]\nfor index,case in enumerate(json.loads((B/'inputs.json').read_bytes())['cases']):\n    if index%2!=shard:continue"
b="mode=sys.argv[1];assert mode in ['control','0','1'];cases=json.loads((B/'inputs.json').read_bytes())['cases']\nif mode=='control':chosen=[c for c in cases if c['control']]\nelse:\n    assert json.loads((V/'control2'/'verification.json').read_bytes())['fixed_input_class_exclusion_certified'];chosen=[c for i,c in enumerate([c for c in cases if not c['control']]) if i%2==int(mode)]\nfor case in chosen:"
assert t.count(a)==1;t=t.replace(a,b);save('s014_split_run',t);print('CAM56 separate producer/verifier/run wrappers generated')
