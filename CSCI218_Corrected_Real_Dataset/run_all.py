"""Run each independent lab activity in sequence."""
import subprocess,sys
from pathlib import Path
r=Path(__file__).resolve().parent
for lab,letters in [(6,'ABCDEFG'),(7,'ABCDEFGH')]:
 for letter in letters:
  print(f'\n===== LAB {lab} ACTIVITY {letter} =====',flush=True)
  subprocess.run([sys.executable,str(r/f'Lab_{lab}_Activities'/f'activity_{letter}.py')],cwd=r,check=True)
print('All activities finished.')
