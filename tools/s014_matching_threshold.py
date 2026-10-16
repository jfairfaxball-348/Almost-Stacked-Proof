"""Directory-only adapter; unchanged complete packed losing-layer algorithm."""
from pathlib import Path
import s014_threshold as core
core.B=Path('evidence/S014/matching')
if __name__=='__main__':core.main()
