import pandas as pd
import numpy as np
import pickle

order = pd.read_csv('../../Data/order_for_analysis.csv')
ads = pd.read_csv('../../Data/t_ads.csv')

product = pd.read_csv('../../Data/t_product.csv')
order['on_dt'] = order['on_dt'].fillna('2016-01-01')
print(len(np.unique(order['shop_id_x'])))
print(len(np.unique(order[['shop_id_x']][order['on_dt']>='2017-02-01'])))
for i in range(8,13):
    print(len(np.unique(order['pid'][order['shop_id_x'] == 2995][order['month'] == i])))
for i in range(1,5):
    print(len(np.unique(order['pid'][order['shop_id_x']==2995][order['month']==i])))



# print(len(np.unique(ads['shop_id'])))
# shop_list = np.unique(order['shop_id_x']).tolist()
# order[order['shop_id_x']==1338].to_csv('demo.csv',index = False)
# ads[ads['shop_id']==1338].to_csv('demo_ads.csv',index=False)
# temp = order[['ord_dt','pid','sale_amt','offer_amt','user_cnt','offer_cnt','rtn_amt','cate','shop_id_x']][order['shop_id_x'] ==2882][order['sale_amt']>100]
# temp = temp[(temp['ord_dt']>='2016-10-01') & (temp['ord_dt']<='2016-12-31')]
# sales = pd.read_csv('../../Data/t_sales_sum.csv')
# print(temp)
# print('*'*100)
# print(len(np.unique(temp['ord_dt'])))
# print(len(np.unique(temp['pid'])))
# print(np.sum(temp.sale_amt))
# print(np.sum(temp.offer_amt))
# print(np.sum(temp.offer_amt)*2.245)
# print(sales[sales['dt']=='2016-09-30'][sales['shop_id']==2882])
# for shop in shop_list:
#     print('*'*100)
#     # sale_amt
#     print(order[['ord_dt','pid','sale_amt','offer_amt','user_cnt','offer_cnt','rtn_amt','cate','shop_id_x']][order['sale_amt'] < 0][order['shop_id_x']==shop])


# 2.245
# 订单销售额为负的情况下，等于 优惠额*(-2.245)
# 销售金额应该就是净利润

# 计算得到销售额 约为 label的 1.12倍左右
