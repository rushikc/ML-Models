import xlrd
import xlwt
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import os

data = pd.read_excel('data.xlsx')


names = data.columns

data.drop_duplicates(inplace=True)  # removing duplicates

data.dropna()


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


for i in range(len(names)):
    IQR_outlier(data[names[i]], names[i])

for i in range(len(names)):
    data[names[i]] = removal_outlier(data[names[i]], names[i])




from scipy.stats import zscore

data.apply(zscore)  # feature scaling

data = (data - data.min()) / (data.max() - data.min())

from sklearn.model_selection import train_test_split

train, test = train_test_split(data, test_size=0.25)  # splitting data
