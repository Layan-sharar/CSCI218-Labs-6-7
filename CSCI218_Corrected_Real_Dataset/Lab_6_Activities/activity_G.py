"""CSCI218 Lab 6 Activity G. Run: python Lab_6_Activities/activity_G.py"""
import sys
from pathlib import Path
sys.path.insert(0,str(Path(__file__).resolve().parent.parent))
from shared import *

raw,x,y,fit=lab6()
assert not x.isna().any().any()
assert all(pd.api.types.is_numeric_dtype(t) for t in x.dtypes)
assert len(x)==len(y)
print('Validated:',x.shape,'target:',len(y))
print('Original source:',DATA.name)
print('Excluded label-missing rows:',int(load_raw().delivery_status.isna().sum()))
