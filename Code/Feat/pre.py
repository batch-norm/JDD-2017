import pandas as pd
import numpy as np
import pickle

"""
    dataset1 dataset2 : training Dataset
    dataset3          : test     Dataset

    dataset1 ： 2016-8 to 2016-12
    dataset2 :  2016-9 to 2017-1
    dataset3 : 2016-12 to 2017-4
"""
order = pd.read_csv('../../Data/t_order.csv')
product = pd.read_csv('../../Data/t_product.csv')
ads = pd.read_csv('../../Data/t_ads.csv')
comment = pd.read_csv('../../Data/t_comment.csv')
train = pd.merge(order, product, how='left', on='pid')
train = train.drop('shop_id_y', axis=1)
train['shop_id'] = train['shop_id_x']
train = train.drop('shop_id_x', axis=1)

# extract time
train_time = pd.DatetimeIndex(train['ord_dt'])
train['month'] = train_time.month
train['day'] = train_time.day
comment_time = pd.DatetimeIndex(comment['create_dt'])
comment['month'] = comment_time.month
comment['day'] = comment_time.day
ads_time = pd.DatetimeIndex(ads['create_dt'])
ads['month'] = ads_time.month
ads['day'] = ads_time.day
# store dataset
order_month_list = []
comment_month_list = []
ads_month_list = []
# for validation
order_month_list.append(train[train['ord_dt'] <= '2016-12-31'])
order_month_list.append(train[(train['ord_dt'] >= '2016-09-01') & (train['ord_dt'] <= '2017-01-31')])
order_month_list.append(train[(train['ord_dt'] >= '2016-12-01') & (train['ord_dt'] <= '2017-04-30')])
comment_month_list.append(comment[comment['create_dt'] <= '2016-12-31'])
comment_month_list.append(comment[(comment['create_dt'] >= '2016-09-01') & (comment['create_dt'] <= '2017-01-31')])
comment_month_list.append(comment[(comment['create_dt'] >= '2016-12-01') & (comment['create_dt'] <= '2017-04-30')])
ads_month_list.append(ads[ads['create_dt'] <= '2016-12-31'])
ads_month_list.append(ads[(ads['create_dt'] >= '2016-09-01') & (ads['create_dt'] <= '2017-01-31')])
ads_month_list.append(ads[(ads['create_dt'] >= '2016-12-01') & (ads['create_dt'] <= '2017-04-30')])
# save validation
print(order_month_list)
with open('order_month.pkl', 'wb') as f:
    pickle.dump(order_month_list, f,-1)
with open('comment_month.pkl', 'wb') as f:
    pickle.dump(comment_month_list, f,-1)
with open('ads_month.pkl', 'wb') as f:
    pickle.dump(ads_month_list, f,-1)
