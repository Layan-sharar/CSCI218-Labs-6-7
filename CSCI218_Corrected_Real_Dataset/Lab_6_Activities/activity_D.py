"""CSCI218 Lab 6 Activity D. Run: python Lab_6_Activities/activity_D.py"""
import sys
from pathlib import Path
sys.path.insert(0,str(Path(__file__).resolve().parent.parent))
from shared import *

raw=clean_target(load_raw())
x,fit=make_features(raw)
print('Categorical columns:',CAT)
print('One-hot feature names:',fit[2].get_feature_names_out(CAT).tolist())
print('Encoded first five:\n',x.head().to_string())
print('Why not LabelEncoder? Unordered categories would receive misleading artificial ranks.')
