"""CSCI218 Lab 7 Activity B. Run: python Lab_7_Activities/activity_B.py"""
import sys
from pathlib import Path
sys.path.insert(0,str(Path(__file__).resolve().parent.parent))
from shared import *

raw,xtr,xte,ytr,yte,fit=lab7()
print('Training:',len(xtr),'test:',len(xte))
print('Train distribution:',ytr.value_counts(normalize=True).to_dict())
print('Test distribution:',yte.value_counts(normalize=True).to_dict())
print('Majority-class baseline:',round(yte.value_counts(normalize=True).max(),4))
