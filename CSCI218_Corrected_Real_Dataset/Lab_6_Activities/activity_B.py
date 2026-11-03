"""CSCI218 Lab 6 Activity B. Run: python Lab_6_Activities/activity_B.py"""
import sys
from pathlib import Path
sys.path.insert(0,str(Path(__file__).resolve().parent.parent))
from shared import *

raw=clean_target(load_raw())
y=(raw.delivery_status=='On_Time').astype(int)
X=raw.drop(columns=['delivery_status'])
print('Target: delivery_status (On_Time=1, Delayed=0)')
print('X:',X.shape,'y:',y.shape)
print(y.value_counts().to_string())
print(X.head().to_string())
