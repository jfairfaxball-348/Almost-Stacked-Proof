import json,sys
from pathlib import Path
import s014_indexed_drup as checker
checker.B=Path('evidence/S014/core_proof');checker.V=Path('evidence/S014/core_proof_replay')
if __name__=='__main__':
    D=checker.B/sys.argv[1]
    if json.loads((D/'result.json').read_bytes())['status']=='UNSAT_AWAITING_INDEPENDENT_CERTIFICATE':checker.main()
    else:print('UNKNOWN: no UNSAT proof to replay',flush=True)
