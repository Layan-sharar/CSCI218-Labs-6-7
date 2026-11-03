"""CSCI218 Lab 7 Activity A. Run: python Lab_7_Activities/activity_A.py"""
import sys
from pathlib import Path
sys.path.insert(0,str(Path(__file__).resolve().parent.parent))
from shared import *

raw,xtr,xte,ytr,yte,fit=lab7()
print('Original supplied data:',DATA.name)
print('Rows after target filtering:',len(raw))
print('Prepared train:',xtr.shape,'test:',xte.shape)
print('Nulls:',int(xtr.isna().sum().sum()+xte.isna().sum().sum()))
print('All numerical:',all(pd.api.types.is_numeric_dtype(t) for t in xtr.dtypes))
print('Training-only fitted preprocessing prevents leakage.')
