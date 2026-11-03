"""CSCI218 Lab 7 Activity D. Run: python Lab_7_Activities/activity_D.py"""
import sys
from pathlib import Path
sys.path.insert(0,str(Path(__file__).resolve().parent.parent))
from shared import *

raw,xtr,xte,ytr,yte,fit,rf,pred=model()
print('Train accuracy:',accuracy_score(ytr,rf.predict(xtr)))
print('Test accuracy:',accuracy_score(yte,pred))
print('Baseline:',yte.value_counts(normalize=True).max())
cm=confusion_matrix(yte,pred,labels=[0,1])
print('Confusion matrix [[actual late/pred late, actual late/pred on time],[actual on time/pred late, actual on time/pred on time]]:\n',cm)
ConfusionMatrixDisplay(cm,display_labels=['Delayed','On_Time']).plot()
save_plot('lab7_confusion_matrix.png')
