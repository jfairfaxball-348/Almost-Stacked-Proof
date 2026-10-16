"""Balanced interface cases through unchanged full sparse producer."""
from pathlib import Path
import s014_threshold as producer
producer.B=Path('evidence/S014/balanced')
if __name__=='__main__':producer.main()
