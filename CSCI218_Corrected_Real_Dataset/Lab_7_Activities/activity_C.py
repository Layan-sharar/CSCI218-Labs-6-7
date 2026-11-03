"""CSCI218 Lab 7 Activity C. Run: python Lab_7_Activities/activity_C.py"""
import sys
from pathlib import Path
sys.path.insert(0,str(Path(__file__).resolve().parent.parent))
from shared import *

raw,xtr,xte,ytr,yte,fit,rf,pred=model()
print('Trained RandomForestClassifier with',len(rf.estimators_),'trees')
