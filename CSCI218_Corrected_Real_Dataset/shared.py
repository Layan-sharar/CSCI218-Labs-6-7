"""Shared lab utilities. Uses the supplied 1M-row compressed CSV, never simulated data."""
from pathlib import Path
import os
import numpy as np
import pandas as pd
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
from sklearn.impute import SimpleImputer
from sklearn.preprocessing import OneHotEncoder
from sklearn.feature_selection import SelectKBest, chi2
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score, confusion_matrix, ConfusionMatrixDisplay
ROOT=Path(__file__).resolve().parent
DATA=ROOT/'data'/'humanitarian_shipments_1M.csv.gz'
PLOTS=ROOT/'plots';PLOTS.mkdir(exist_ok=True)
# Set CSCI218_SAMPLE_ROWS=0 to use all rows (needs much more RAM and CPU).
SAMPLE_ROWS=int(os.getenv('CSCI218_SAMPLE_ROWS','20000'))
CAT=['record_source','origin_hub','destination_region','cargo_category','priority_level','transport_mode','cold_chain_required']
NUM=['weight_kg','volume_m3','num_pallets','declared_value_usd','distance_km','beneficiaries_targeted','customs_clearance_days','fuel_price_index']
DROP=['shipment_id','dispatch_date','country_office_code','handler_notes','cold_chain_temp_c','weight_lbs','days_late']
TARGET='delivery_status'

def load_raw():
    df=pd.read_csv(DATA,compression='gzip')
    if SAMPLE_ROWS>0 and len(df)>SAMPLE_ROWS:
        df=df.sample(n=SAMPLE_ROWS,random_state=218).sort_index().reset_index(drop=True)
    return df

def clean_target(df):
    return df[df[TARGET].isin(['On_Time','Delayed'])].copy()

def make_features(raw, fit=None):
    x=raw[NUM+CAT].copy()
    # Negative/zero weights are invalid; high positive values remain for human review.
    x.loc[x.weight_kg<=0,'weight_kg']=np.nan
    x.loc[x.declared_value_usd<0,'declared_value_usd']=np.nan
    if fit is None:
        ni=SimpleImputer(strategy='median');ci=SimpleImputer(strategy='most_frequent')
        ni.fit(x[NUM]);ci.fit(x[CAT]); enc=OneHotEncoder(handle_unknown='ignore',sparse_output=False)
        enc.fit(pd.DataFrame(ci.transform(x[CAT]),columns=CAT,index=x.index))
        fit=(ni,ci,enc)
    ni,ci,enc=fit
    xn=pd.DataFrame(ni.transform(x[NUM]),columns=NUM,index=x.index)
    xc=pd.DataFrame(ci.transform(x[CAT]),columns=CAT,index=x.index)
    xe=pd.DataFrame(enc.transform(xc),columns=enc.get_feature_names_out(CAT),index=x.index)
    return pd.concat([xn,xe],axis=1),fit

def lab6():
    raw=clean_target(load_raw())
    y=(raw[TARGET]=='On_Time').astype(int)
    x,fit=make_features(raw)
    return raw,x,y,fit

def lab7():
    raw=clean_target(load_raw());y=(raw[TARGET]=='On_Time').astype(int)
    tr,te=train_test_split(np.arange(len(raw)),test_size=.25,random_state=42,stratify=y)
    # Fit imputation/encoding ONLY on training rows to prevent data leakage.
    xtr,fit=make_features(raw.iloc[tr]);xte,_=make_features(raw.iloc[te],fit)
    ytr=y.iloc[tr];yte=y.iloc[te]
    return raw,xtr,xte,ytr,yte,fit

def model():
    raw,xtr,xte,ytr,yte,fit=lab7()
    rf=RandomForestClassifier(n_estimators=100,random_state=42,n_jobs=-1)
    rf.fit(xtr,ytr)
    pred=rf.predict(xte)
    return raw,xtr,xte,ytr,yte,fit,rf,pred

def save_plot(name):
    plt.tight_layout();p=PLOTS/name;plt.savefig(p,dpi=130,bbox_inches='tight');plt.close();print('Saved:',p.relative_to(ROOT))
