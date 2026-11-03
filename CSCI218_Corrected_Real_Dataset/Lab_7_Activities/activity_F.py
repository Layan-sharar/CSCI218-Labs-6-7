"""CSCI218 Lab 7 Activity F. Run: python Lab_7_Activities/activity_F.py"""
import sys
from pathlib import Path
sys.path.insert(0,str(Path(__file__).resolve().parent.parent))
from shared import *

raw,xtr,xte,ytr,yte,fit=lab7()
rows=[]
for trees in [1,5,10,50,100,200]:
 rf=RandomForestClassifier(n_estimators=trees,random_state=42,n_jobs=-1)
 rf.fit(xtr,ytr)
 rows.append((trees,accuracy_score(yte,rf.predict(xte))))
print(pd.DataFrame(rows,columns=['Trees','Test accuracy']).to_string(index=False))
plt.figure(figsize=(8,4))
plt.plot(*zip(*rows),marker='o')
plt.xlabel('Number of trees')
plt.ylabel('Test accuracy')
save_plot('lab7_tree_comparison.png')
