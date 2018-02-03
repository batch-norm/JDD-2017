import xgboost as xgb
import pandas as pd
import numpy as np
from bayes_opt import BayesianOptimization
from sklearn.model_selection import cross_val_score
from xgboost.sklearn import XGBRegressor
from sklearn import preprocessing

dataset1 = pd.read_csv('../../Data/train_dataset1.csv')
dataset2 = pd.read_csv('../../Data/train_dataset2.csv')
sales = pd.read_csv('../../Data/t_sales_sum.csv')
# duplicate value in sales
dataset1_y_dict = {}
dataset1_y = []

# for dataset1_y
def make_y_1(line):
    dataset1_y_dict[int(line['shop_id'])] = float(line['sale_amt_3m'])

sales[['shop_id', 'sale_amt_3m']][sales['dt'] == '2017-01-31'].apply(lambda line: make_y_1(line), axis=1)
dataset1_y_dict = sorted(dataset1_y_dict.items(), key=lambda item: item[0])
for sale in dataset1_y_dict:
    dataset1_y.append(sale[1])

# for dataset12_y
# label
dataset1_y = np.log1p(np.array(dataset1_y))
# train Data
# dataset1 = dataset1.drop(['shop_id'], axis=1)
# dataset2 = dataset2.drop(['shop_id'], axis=1)

d_train = xgb.DMatrix(dataset1, label=pd.Series(dataset1_y))
d_test = xgb.DMatrix(dataset2)


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
    'eta': 0.01,
    'seed': 0,
    'silent': 1
}
# train
watchlist1 = [(d_train, 'train')]
mdl = xgb.train(params, d_train, 150000, watchlist1, early_stopping_rounds=500, feval=wmae, maximize=True,
                 verbose_eval=10)

# submission
pred = mdl.predict(d_test)
submission = pd.DataFrame({
    'shop_id': range(1, 3001)
})
submission['pred'] = np.expm1(pred)
submission.to_csv('../../Output/submission.csv', index=False, header=False, encoding='utf-8')
# save feature score
feature_score = mdl.get_fscore()
feature_score = sorted(feature_score.items(), key=lambda x: x[1], reverse=True)
fs = []
for (key, value) in feature_score:
    fs.append('{0},{1}\n'.format(key, value))
with open('xgb_feature_score.csv', 'w') as f:
    f.writelines('feature,score\n')
    f.writelines(fs)
