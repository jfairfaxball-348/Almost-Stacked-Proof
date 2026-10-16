"""Balanced interface cases through independent unchanged full tuple replay."""
from pathlib import Path
import s014_threshold_verify as verifier
verifier.B=Path('evidence/S014/balanced')
if __name__=='__main__':verifier.main()
