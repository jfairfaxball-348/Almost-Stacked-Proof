"""Directory-only adapter; unchanged independent tuple-coordinate checker."""
from pathlib import Path
import s014_threshold_verify as core
core.B=Path('evidence/S014/matching')
if __name__=='__main__':core.main()
