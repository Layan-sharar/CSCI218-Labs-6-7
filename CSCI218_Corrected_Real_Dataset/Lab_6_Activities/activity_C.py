"""CSCI218 Lab 6 Activity C. Run: python Lab_6_Activities/activity_C.py"""
import sys
from pathlib import Path
sys.path.insert(0,str(Path(__file__).resolve().parent.parent))
from shared import *

raw=clean_target(load_raw())
X=raw.drop(columns=['delivery_status']+DROP)
print('Dropped:',DROP)
print('Reasons: IDs, dates, free text, highly sparse temperature, redundant pounds, and post-delivery days_late (target leakage).')
print('Remaining:',X.columns.tolist())
