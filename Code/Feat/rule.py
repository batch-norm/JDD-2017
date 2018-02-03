

import numpy as np
import pandas as pd
import math
shop_sale={}
shop_sale_2={}
shop_sale_3={}

a=pd.read_csv('t_order.csv',chunksize=100000)
for chunk in a:
    print("1")
    date=np.array(chunk['ord_dt'])
    sale=np.array(chunk['sale_amt'])
    shop=np.array(chunk['shop_id'])
    for i in range(len(date)):
        temp=date[i].split("-")
        temp_id=str(shop[i])
        if int(temp[1])==4:
            if temp_id not in shop_sale:
                shop_sale[temp_id]=sale[i]
            else:
                shop_sale[temp_id]=shop_sale[temp_id]+sale[i]
        if int(temp[1])==3:
            if temp_id not in shop_sale_2:
                shop_sale_2[temp_id]=sale[i]
            else:
                shop_sale_2[temp_id]=shop_sale_2[temp_id]+sale[i]
        if int(temp[1])==2:
            if temp_id not in shop_sale_3:
                shop_sale_3[temp_id]=sale[i]
            else:
                shop_sale_3[temp_id]=shop_sale_3[temp_id]+sale[i]
shop_sale=pd.Series(shop_sale).reset_index()
shop_sale.columns=['shop_id','month4']
shop_sale_2=pd.Series(shop_sale_2).reset_index()
shop_sale_2.columns=['shop_id','month3']
shop_sale_3=pd.Series(shop_sale_3).reset_index()
shop_sale_3.columns=['shop_id','month2']
shop_sale=shop_sale.merge(shop_sale_2,on='shop_id',how='left').merge(shop_sale_3,on='shop_id',how='left')

shop_sale_e=(shop_sale['month4']*0.6+shop_sale['month3']*0.3+shop_sale['month2']*0.1)
final=pd.concat([shop_sale,shop_sale_e],axis=1)
final.to_csv("all.csv",index=False)