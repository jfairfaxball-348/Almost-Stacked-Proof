import sys
from pathlib import Path
import s014_tail_screen_verify as core
core.B=Path('evidence/S014/highpile_cegis')/sys.argv[1]/'potential';sys.argv=['verify','0']
if __name__=='__main__':core.main()
