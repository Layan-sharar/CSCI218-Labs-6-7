"""CSCI218 Lab 6 Activity F. Run: python Lab_6_Activities/activity_F.py"""
import sys
from pathlib import Path
sys.path.insert(0,str(Path(__file__).resolve().parent.parent))
from shared import *

raw,x,y,fit=lab6()
plt.figure(figsize=(9,4))
plt.boxplot(raw.weight_kg.dropna(),vert=False)
plt.xlabel('Weight (kg)')
plt.title('Review extreme shipment weights')
save_plot('lab6_weight_outliers.png')
print('Non-positive weights:',int((raw.weight_kg<=0).sum()))
print('Large positive weights are not automatically discarded.')
sel=SelectKBest(chi2,k=min(8,x.shape[1])).fit(x,y)
print('Selected:',x.columns[sel.get_support()].tolist())
print('Scores:',sorted(zip(x.columns,sel.scores_),key=lambda t:-t[1])[:8])
