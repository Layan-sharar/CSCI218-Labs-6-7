"""CSCI218 Lab 7 Activity G. Run: python Lab_7_Activities/activity_G.py"""
import sys
from pathlib import Path
sys.path.insert(0,str(Path(__file__).resolve().parent.parent))
from shared import *

raw,xtr,xte,ytr,yte,fit,rf,pred=model()
new=pd.DataFrame({'record_source':['Warehouse_Scan','Field_Report','Warehouse_Scan'],'origin_hub':['DXB_Hub','NBO_Hub','ACC_Hub'],'destination_region':['Middle_East','East_Africa','Latin_America'],'cargo_category':['Medical','Shelter','Food'],'priority_level':['Critical','High','Medium'],'transport_mode':['Air','Sea','Road'],'cold_chain_required':['Yes','No','No'],'weight_kg':[1500,42000,9000],'volume_m3':[3,110,24],'num_pallets':[2,45,12],'declared_value_usd':[20000,150000,45000],'distance_km':[2200,6500,800],'beneficiaries_targeted':[4000,12000,8000],'customs_clearance_days':[1,9,np.nan],'fuel_price_index':[100,105,99]},index=['Shipment A','Shipment B','Shipment C'])
newx,_=make_features(new,fit)
p=rf.predict(newx)
proba=rf.predict_proba(newx)[:,list(rf.classes_).index(1)]
print(pd.DataFrame({'Prediction':np.where(p==1,'On_Time','Delayed'),'Probability_on_time':proba},index=new.index).to_string())
print('Unseen hub/category labels are handled with handle_unknown=ignore.')
