"""CSCI218 Lab 6 Activity E. Run: python Lab_6_Activities/activity_E.py"""
import sys
from pathlib import Path
sys.path.insert(0,str(Path(__file__).resolve().parent.parent))
from shared import *

raw=clean_target(load_raw())
print('Missing before:\n',raw[NUM+CAT].isna().sum().to_string())
x,fit=make_features(raw)
print('Median numerical imputation, most-frequent categorical imputation.')
print('Missing after:',int(x.isna().sum().sum()))
print('Missing target rows excluded:',int(load_raw().delivery_status.isna().sum()))
