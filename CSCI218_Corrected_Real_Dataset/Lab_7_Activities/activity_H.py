"""CSCI218 Lab 7 Activity H. Run: python Lab_7_Activities/activity_H.py"""
import sys
from pathlib import Path
sys.path.insert(0,str(Path(__file__).resolve().parent.parent))
from shared import *

raw,xtr,xte,ytr,yte,fit,rf,pred=model()
assert xtr.isna().sum().sum()==0 and xte.isna().sum().sum()==0
assert len(pred)==len(yte)
print('Validation successful. Test accuracy:',round(accuracy_score(yte,pred),4))
print('Baseline:',round(yte.value_counts(normalize=True).max(),4))
