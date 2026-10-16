"""Separate unchanged complete canonical-parent verifier, new scoped inputs."""
from pathlib import Path
import s014_threshold_verify as verifier
verifier.B=Path('evidence/S014/book_family')
if __name__=='__main__':verifier.main()
