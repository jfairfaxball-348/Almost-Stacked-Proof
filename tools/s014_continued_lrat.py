from pathlib import Path
import s014_lrat_verify as checker
checker.B=Path('evidence/S014/continued_lrat');checker.P=Path('evidence/S014/continued_cegis')
if __name__=='__main__':checker.main()
