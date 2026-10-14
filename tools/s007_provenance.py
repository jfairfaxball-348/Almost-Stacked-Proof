"""Read-only entry reconciliation and primary-source digest refresh."""
import hashlib
import json
import platform
import re
import subprocess
import sys
import urllib.request
from pathlib import Path

OUT = Path('evidence/S007')
REPO = 'jfairfaxball-348/Almost-Stacked-Proof'

def write(name, value):
    (OUT / name).write_text(json.dumps(value, indent=2) + '\n', encoding='utf-8', newline='\n')

def api(path):
    p = subprocess.run(['gh', 'api', path], capture_output=True, text=True, encoding='utf-8')
    try:
        body = json.loads(p.stdout)
    except json.JSONDecodeError:
        body = p.stdout
    return {'exit_code': p.returncode, 'body': body, 'stderr': p.stderr}

def main():
    root = f'repos/{REPO}'
    head = '74feae2559af1ddc855febbd0da9693faf51ef22'
    main_sha = 'e320a3c80da3807beb031c8b2dab69bfb807805c'
    requests = {
        'main_ref': f'{root}/git/ref/heads/main',
        'main_commit': f'{root}/git/commits/{main_sha}',
        'previous_pr': f'{root}/pulls/8',
        'previous_commits': f'{root}/pulls/8/commits',
        'branches': f'{root}/branches?per_page=100',
        'prs': f'{root}/pulls?state=all&per_page=100',
        'protection': f'{root}/branches/main/protection',
        'rulesets': f'{root}/rulesets',
    }
    for label, sha in [('main', main_sha), ('head', head)]:
        requests[f'{label}_runs'] = f'{root}/actions/runs?head_sha={sha}&per_page=100'
        requests[f'{label}_checks'] = f'{root}/commits/{sha}/check-runs?per_page=100'
        requests[f'{label}_status'] = f'{root}/commits/{sha}/status'
    result = {}
    for name, path in requests.items():
        result[name] = api(path)
        write(f'entry_{name}.json', result[name])
    for label in ('main', 'head'):
        jobs = []
        for run in result[f'{label}_runs']['body']['workflow_runs']:
            jobs.append({'run_id': run['id'], 'response': api(f"{root}/actions/runs/{run['id']}/jobs?per_page=100")})
        write(f'entry_{label}_jobs.json', jobs)
    assert result['main_ref']['body']['object']['sha'] == main_sha
    assert result['previous_pr']['body']['head']['sha'] == head
    assert result['previous_pr']['body']['merge_commit_sha'] == main_sha
    assert [c['sha'] for c in result['previous_commits']['body']] == [head]
    assert [p['sha'] for p in result['main_commit']['body']['parents']] == ['876e2a36a1fe15c82e3f7085c233f3f9f49ed2d5', head]
    source = {}
    previous = json.loads(Path('evidence/S006/source_refresh.json').read_text())
    for ident in ('2610.09650', '2604.22341'):
        page = urllib.request.urlopen(f'https://arxiv.org/abs/{ident}', timeout=60).read()
        pdf = urllib.request.urlopen(f'https://arxiv.org/pdf/{ident}v1', timeout=60).read()
        versions = sorted(set(re.findall(rb'\[v(\d+)\]', page)))
        source[ident] = {'versions': [v.decode() for v in versions], 'abs_sha256': hashlib.sha256(page).hexdigest(),
                         'pdf_sha256': hashlib.sha256(pdf).hexdigest(), 'pdf_bytes': len(pdf),
                         'pdf_unchanged': hashlib.sha256(pdf).hexdigest() == previous[ident]['pdf_sha256']}
        assert source[ident]['pdf_unchanged'] and versions == [b'1']
    write('source_refresh.json', source)
    write('environment.json', {'python': sys.version, 'platform': platform.platform(), 'machine': platform.machine(),
                              'research_execution': 'local Windows', 'date': '2026-10-14', 'configuration_symmetry': 'none'})
    counts = {}
    for session in ('S003', 'S004', 'S005', 'S006'):
        count = 0
        for line in Path(f'evidence/{session}/HASHES.md').read_text(encoding='utf-8').splitlines():
            m = re.fullmatch(r'`([0-9a-f]{64})`\s+`([^`]+)`.*', line.strip().lstrip('- '))
            if m and not m[2].startswith('scratch:'):
                index_path = Path('evidence/S007/frozen_s006_index.json')
                frozen = {p:info['snapshot'] for p,info in json.loads(index_path.read_text())['files'].items()} if session == 'S006' and index_path.exists() else {}
                historical = Path(frozen.get(m[2],m[2]))
                if not historical.exists():
                    historical = Path(m[2])
                assert hashlib.sha256(historical.read_bytes()).hexdigest() == m[1], m[2]
                count += 1
        counts[session] = count
    write('inherited_hashes.json', counts)
    print(json.dumps({'entry_reconciled': True, 'sources': source, 'inherited_hashes': counts}))

if __name__ == '__main__':
    main()
