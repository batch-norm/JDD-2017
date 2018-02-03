
import lightgbm as lgb
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

rem=[]
me={}
ad=pd.read_csv('new_ad.csv')
comment=pd.read_csv('new_comment.csv')
order=pd.read_csv('new_order.csv')
all_sum=pd.read_csv('new_sum.csv')
temp_sum=pd.read_csv('new_sum1.csv')
temp_sum2=pd.read_csv('new_sum2.csv')
#last_2=pd.read_csv('new_sum4.csv')
test=pd.read_csv('new_test.csv')
#shop_size=pd.read_csv('shop_size.csv')
#product=pd.read_csv('product_new.csv')
#product2=pd.read_csv('product_new2.csv')
#shop_size=pd.read_csv('shop_size.csv')
#day0115=pd.read_csv('day_0115.csv')
#day1630=pd.read_csv('day_1630.csv')

#day2130=pd.read_csv('day_2130.csv')
#day1630=pd.read_csv('day_1630.csv')
#day26=pd.read_csv('day_26.csv')
#day27=pd.read_csv('day_27.csv')
#day28=pd.read_csv('day_28.csv')
#day29=pd.read_csv('day_29.csv')
#day30=pd.read_csv('day_30.csv')
#以上包括各种时间序列切分，跑出来不同结果，最后取平均


'''shop=np.array(test['shop_id'])
for i in range(len(shop)):
 
    temp_id=str(shop[i])+"201704"
    rem.append(temp_id)
rem=pd.DataFrame(rem)
rem.columns=['shop_month']
test=pd.concat([rem,test],axis=1)


test.to_csv("new_test.csv",index=False)'''

temp_sum=temp_sum.drop_duplicates(['shop_month_ago'])


X_train=all_sum.merge(ad,on='shop_month',how='left').merge(comment,on='shop_month',how='left').merge(order,on='shop_month',how='left')
X_train=X_train.merge(temp_sum,on='shop_month_ago',how='left')
X_train=X_train.merge(temp_sum2,on='shop_month_last',how='left')




#X_train=X_train.merge(shop_size,on='shop_id',how='left')
#X_train=X_train.merge(last_2,on='shop_month_last_2',how='left')
#X_train=X_train.merge(day1120,on='shop_month',how='left')
#X_train=X_train.merge(day0115,on='shop_month',how='left')
#X_train=X_train.merge(day26,on='shop_month',how='left')
#X_train=X_train.merge(day27,on='shop_month',how='left')
#X_train=X_train.merge(day28,on='shop_month',how='left')
#X_train=X_train.merge(day29,on='shop_month',how='left')
#X_train=X_train.merge(day30,on='shop_month',how='left')
#X_train=X_train.merge(day1630,on='shop_month',how='left')
#X_train=X_train.merge(day2130,on='shop_month',how='left')




#X_train=X_train.merge(shop_size,on='shop_id',how='left')
#X_train=X_train.merge(product,on='shop_month',how='left')

X_train_sale=X_train['sale']-X_train['sale_2']
X_train_sale=pd.DataFrame(X_train_sale)
X_train_sale.columns=['sale_minus']
X_train=pd.concat([X_train,X_train_sale],axis=1)

#X_train_sale_last=X_train['sale']/X_train['Last_3']
#X_train_sale_last=pd.DataFrame(X_train_sale_last)
#X_train_sale_last.columns=['sale_bili']
#X_train=pd.concat([X_train,X_train_sale_last],axis=1)

X_test=test.merge(ad,on='shop_month',how='left').merge(comment,on='shop_month',how='left').merge(order,on='shop_month',how='left')
X_test=X_test.merge(temp_sum,on='shop_month_ago',how='left')
X_test=X_test.merge(temp_sum2,on='shop_month_last',how='left')


#X_test=X_test.merge(shop_size,on='shop_id',how='left')
#X_test=X_test.merge(last_2,on='shop_month_last_2',how='left')
#X_test=X_test.merge(day1120,on='shop_month',how='left')
#X_test=X_test.merge(day,on='shop_month',how='left')
#X_test=X_test.merge(day26,on='shop_month',how='left')
#X_test=X_test.merge(day27,on='shop_month',how='left')
#X_test=X_test.merge(day28,on='shop_month',how='left')
#X_test=X_test.merge(day29,on='shop_month',how='left')
#X_test=X_test.merge(day30,on='shop_month',how='left')
#X_test=X_test.merge(day1630,on='shop_month',how='left')
#X_test=X_test.merge(day2130,on='shop_month',how='left')


#X_test=X_test.merge(shop_size,on='shop_id',how='left')
#X_test=X_test.merge(product,on='shop_month',how='left')


X_test_sale=X_test['sale']-X_test['sale_2']
X_test_sale=pd.DataFrame(X_test_sale)
X_test_sale.columns=['sale_minus']
X_test=pd.concat([X_test,X_test_sale],axis=1)

#X_test_sale_last=X_test['sale']/X_test['Last_3']
#X_test_sale_last=pd.DataFrame(X_test_sale_last)
#X_test_sale_last.columns=['sale_bili']
#X_test=pd.concat([X_test,X_test_sale_last],axis=1)




X_train=X_train.dropna(subset=['good', 'mid', 'bad','dis','sale','comment'], how='all')

y_train=X_train['sale_amt_3m']


need=test['shop_id']
del X_train['shop_id']
del X_test['shop_id']
del X_train['sale_amt_3m']
del X_test['pre']



del X_train['shop_month']
del X_test['shop_month']
del X_train['shop_month_ago']
del X_test['shop_month_ago']
del X_train['shop_month_last']
del X_test['shop_month_last']

del X_train['dt']


lgb_train = lgb.Dataset(X_train, y_train)

params = {
    'task': 'train',
    'boosting_type': 'gbdt',
    'objective': 'regression_l1',
    'metric': {'l1', 'mae'},
    'num_leaves': 31,
    'learning_rate': 0.01,
    'feature_fraction': 0.9,
    'bagging_fraction': 0.8,
    'bagging_freq': 5,
    'verbose': 0
}
'''sb=lgb.cv(params,
       lgb_train,
       nfold=5,
       num_boost_round=500,
       early_stopping_rounds=5
       )'''
gbm = lgb.train(params,
                lgb_train,
                num_boost_round=2158,
                valid_sets=lgb_train,  # eval training data
                )

y_pred = gbm.predict(X_test, num_iteration=2158)

for i in range(len(y_pred)):
    if y_pred[i] not in me:
        me[y_pred[i]]=1
    else:
        me[y_pred[i]]=me[y_pred[i]]+1



a=gbm.feature_importance()
ax = lgb.plot_importance(gbm, max_num_features=15)
plt.show()
y_pred=pd.DataFrame(y_pred)
y_pred.columns=['pre']
final=pd.concat([need,y_pred],axis=1)

final.to_csv('final.csv',index=False)
