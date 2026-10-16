"""Directory adapter for unchanged full losing-layer producer."""
from pathlib import Path
import s014_threshold as core
core.B=Path('evidence/S014/buffers')
if __name__=='__main__':core.main()
