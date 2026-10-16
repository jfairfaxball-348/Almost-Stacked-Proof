"""New registered book-star inputs through the unchanged complete producer."""
from pathlib import Path
import s014_threshold as producer
producer.B=Path('evidence/S014/book_family')
if __name__=='__main__':producer.main()
