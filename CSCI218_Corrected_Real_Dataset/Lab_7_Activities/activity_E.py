"""CSCI218 Lab 7 Activity E. Run: python Lab_7_Activities/activity_E.py"""
import sys
from pathlib import Path
sys.path.insert(0,str(Path(__file__).resolve().parent.parent))
from shared import *

raw,xtr,xte,ytr,yte,fit,rf,pred=model()
imp=pd.Series(rf.feature_importances_,index=xtr.columns).sort_values(ascending=False)
print('Top ten:\n',imp.head(10).to_string())
plt.figure(figsize=(9,5))
imp.head(10).sort_values().plot.barh()
plt.xlabel('Importance')
save_plot('lab7_feature_importance.png')
selector=SelectKBest(chi2,k=8).fit(xtr,ytr)
print('Lab6-style chi2 top eight:',xtr.columns[selector.get_support()].tolist())
