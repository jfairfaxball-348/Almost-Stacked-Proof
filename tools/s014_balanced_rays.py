"""Registered balanced graph boxes, through the unchanged exact optimizer."""
from pathlib import Path
import s014_rays as optimizer
optimizer.B=Path('evidence/S014/balanced')
if __name__=='__main__':optimizer.main()
