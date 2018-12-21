import xlrd
import xlwt
import numpy as np
import matplotlib.pyplot as plt
# %matplotlib inline
import neurolab as nl
import pandas as pd
import seaborn as sns
import os
from sklearn.linear_model import LinearRegression
from sklearn.metrics import r2_score
import time

data = pd.read_excel('data1.xlsx')

import statsmodels.api as sm
X = data[['SO2','NOX','BENZENE']]
y = data['PM10']
X = sm.add_constant(X)
model11 = sm.OLS(y, X).fit()
print(model11.summary())









exit()

















del data['FROM DATE']
del data['TO DATE']
del data['VWS']
del data['TEMP']
del data['AT']


names = data.columns



data.drop_duplicates(inplace=True)  # removing duplicates



limit = {}


def IQR_outlier(dt, name):
    q1 = dt.quantile(.25)
    q3 = dt.quantile(.75)
    iqr = q3 - q1
    l_limit = q1 - 1.5 * iqr
    r_limit = q3 + 1.5 * iqr
    l_limit = round(l_limit, 2)
    r_limit = round(r_limit, 2)
    limit[name] = [l_limit, r_limit]


def removal_outlier(st, name):
    st = st[st < limit[name][1]]
    st = st[st > limit[name][0]]
    return st


# for i in range(len(names)):
    # IQR_outlier(data[names[i]], names[i])

# for i in range(len(names)):
    # data[names[i]] = removal_outlier(data[names[i]], names[i])

data = data.dropna()





# data = (data - data.min()) / (data.max() - data.min())

from scipy.stats import zscore
data.apply(zscore)




from sklearn.model_selection import train_test_split

train, test = train_test_split(data, test_size=0.25) #splitting data

train.to_excel('dt1_train.xlsx')
test.to_excel('dt1_test.xlsx')

fh = open('data1.txt','w')


for i in range(len(names)):
    for j in range(len(names)):
        if(names[i]!=names[j]):
            # train[names[i]] = train[names[i]].apply(np.sqrt)
            # train[names[j]] = train[names[j]].apply(np.sqrt)
            # test[names[i]] = test[names[i]].apply(np.sqrt)
            # test[names[j]] = test[names[j]].apply(np.sqrt)

            x_train = train[names[i]]
            y_train = train[names[j]]
            x_test = test[names[i]]
            y_test = test[names[j]]

            x_train = np.array(x_train)
            y_train = np.array(y_train)
            x_test = np.array(x_test)
            y_test = np.array(y_test)

            x_train = x_train.reshape(-1, 1)
            x_test = x_test.reshape(-1, 1)

            clf = LinearRegression(normalize=True)
            clf.fit(x_train, y_train)
            y_pred = clf.predict(x_test)



            n11 = r2_score(y_test, y_pred)
            if(n11 > 0.7):
                print(names[i], 'and', names[j])
                print(n11)
                st1 = names[i] + ' and ' + names[j]+'\n'
                fh.writelines(st1)
                fh.writelines(str(n11))
                fh.writelines('\n')

fh.close()
