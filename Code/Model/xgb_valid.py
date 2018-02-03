import xgboost as xgb
import pandas as pd
import numpy as np
from bayes_opt import BayesianOptimization
from sklearn.model_selection import cross_val_score
from xgboost.sklearn import XGBRegressor
from sklearn import preprocessing

dataset1 = pd.read_csv('../../Data/dataset1.csv')
dataset2 = pd.read_csv('../../Data/dataset2.csv')
dataset3 = pd.read_csv('../../Data/dataset3.csv')
dataset12 = pd.DataFrame(pd.concat([dataset1, dataset2]))
sales = pd.read_csv('../../Data/t_sales_sum.csv')
# duplicate value in sales
dataset1_y_dict = {}
dataset1_y = []


# for dataset1_y
def make_y_1(line):
    dataset1_y_dict[int(line['shop_id'])] = float(line['sale_amt_3m'])


sales[['shop_id', 'sale_amt_3m']][sales['dt'] == '2016-12-31'].apply(lambda line: make_y_1(line), axis=1)
dataset1_y_dict = sorted(dataset1_y_dict.items(), key=lambda item: item[0])
for sale in dataset1_y_dict:
    dataset1_y.append(sale[1])
# for dataset2_y
dataset2_y_dict = {}
dataset2_y = []


def make_y_2(line):
    dataset2_y_dict[int(line['shop_id'])] = float(line['sale_amt_3m'])


sales[['shop_id', 'sale_amt_3m']][sales['dt'] == '2017-01-31'].apply(lambda line: make_y_2(line), axis=1)
dataset2_y_dict = sorted(dataset2_y_dict.items(), key=lambda item: item[0])
for sale in dataset2_y_dict:
    dataset2_y.append(sale[1])
# for dataset12_y
dataset12_y = dataset1_y + dataset2_y
# label
dataset1_y = np.log1p(np.array(dataset1_y))
dataset2_y = np.log1p(np.array(dataset2_y))
dataset12_y = np.log1p(np.array(dataset12_y))
# train Data


# dataset1 = dataset1.drop(['shop_id', 'shop_cat'], axis=1)
# dataset2 = dataset2.drop(['shop_id', 'shop_cat'], axis=1)
# dataset12 = dataset12.drop(['shop_id', 'shop_cat'], axis=1)
# # test Data
# dataset3 = dataset3.drop(['shop_id', 'shop_cat'], axis=1)


# drop features
# dataset1 = dataset1.drop(['average_sales_amount_increase_rate'], axis=1)
# dataset2 = dataset2.drop(['average_sales_amount_increase_rate'], axis=1)
# dataset12 = dataset12.drop(['average_sales_amount_increase_rate'], axis=1)
# dataset3 = dataset3.drop(['average_sales_amount_increase_rate'], axis=1)


def XRwmae(pred, y):
    y = np.expm1(y)
    pred = np.expm1(pred)
    sum_abs = []
    for y1, y2 in zip(pred, y):
        sum_abs.append(np.abs(y1 - y2))
    return 1 - (np.sum(sum_abs) / np.sum(y))


# XR = XGBRegressor(
#     n_estimators=2000,
#     learning_rate=0.1,
#     booster='gbtree',
#     seed=0,
#     objective='reg:linear',
#     max_depth=5)
# XR.fit(dataset1, dataset1_y)
# XRpred = XR.predict(dataset2)
# acc = XRwmae(XRpred, dataset2_y)
# ft_weights = pd.DataFrame(XR.feature_importances_, columns=['weights'], index=dataset1.columns)
# print(ft_weights)
# print(1 - acc)

d_train1 = xgb.DMatrix(dataset1, label=pd.Series(dataset1_y))
d_train2 = xgb.DMatrix(dataset2, label=pd.Series(dataset2_y))
d_train12 = xgb.DMatrix(dataset12, label=pd.Series(dataset12_y))
d_test = xgb.DMatrix(dataset3, label=dataset3.values)


# evaluation function
def wmae(pred, y):
    y = y.get_label()
    y = np.expm1(y)
    pred = np.expm1(pred)
    sum_abs = []
    for y1, y2 in zip(pred, y):
        sum_abs.append(np.abs(y1 - y2))
    return 'wmae', 1 - (np.sum(sum_abs) / np.sum(y))


# xgb
params = {
    'booster': 'gbtree',
    'objective': 'reg:linear',
    'max_depth': 8,
    'eta': 0.1,
    'seed': 0,
    'silent': 1
}
# validation
watchlist1 = [(d_train1, 'd_train1'), (d_train2, 'd_train2')]
mdl1 = xgb.train(params, d_train1, 100000, watchlist1, early_stopping_rounds=200, feval=wmae, maximize=True,
                 verbose_eval=10)
# watchlist2 = [(d_train2, 'd_train2')]
# mdl2 = xgb.train(params, d_train2, 10000, watchlist2, early_stopping_rounds=150, feval=wmae, maximize=True,
#                  verbose_eval=10)
print('best WMAE:' + str(1 - mdl1.best_score))
# no validation
watchlist = [(d_train12, 'train')]
mdl = xgb.train(params, d_train12, 100000, watchlist, early_stopping_rounds=200, feval=wmae, maximize=True,
                verbose_eval=10)

# submission
pred1 = mdl1.predict(d_test)
#pred2 = mdl2.predict(d_test)
pred3 = mdl.predict(d_test)
submission = pd.DataFrame({
    'shop_id': range(1, 3001)
})
submission['pred'] = np.expm1(pred3)
submission.to_csv('../../Output/submission.csv', index=False, header=False, encoding='utf-8')
submission['dataset2_y'] = np.expm1(dataset2_y)
submission.to_csv('../../Output/reference.csv', index=False, header=False, encoding='utf-8')
# save feature score
feature_score = mdl.get_fscore()
feature_score = sorted(feature_score.items(), key=lambda x: x[1], reverse=True)
fs = []
for (key, value) in feature_score:
    fs.append('{0},{1}\n'.format(key, value))
with open('xgb_feature_score.csv', 'w') as f:
    f.writelines('feature,score\n')
    f.writelines(fs)
