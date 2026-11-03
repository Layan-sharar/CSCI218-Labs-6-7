"""CSCI218 Lab 6 Activity A. Run: python Lab_6_Activities/activity_A.py"""
import sys
from pathlib import Path
sys.path.insert(0,str(Path(__file__).resolve().parent.parent))
from shared import *

raw=load_raw()
print('Dataset sample shape:',raw.shape)
print('First 10 rows:')
print(raw.head(10).to_string())
raw.info()
print(raw.describe(include='all').to_string())
print('Numeric:',raw.select_dtypes('number').columns.tolist())
print('Categorical:',raw.select_dtypes(exclude='number').columns.tolist())
print('Missing:\n',raw.isna().sum().to_string())
