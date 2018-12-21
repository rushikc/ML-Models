import xlrd
import xlwt
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import os
data = pd.read_excel('data.xlsx')

names = data.columns

limit = {}
def IQR_outlier(dt,name):

    q1 = dt.quantile(.25)
    q3 = dt.quantile(.75)
    iqr = q3 -q1
    l_limit = q1 - 1.5*iqr
    r_limit = q3 + 1.5*iqr
    l_limit = round(l_limit,2)
    r_limit = round(r_limit,2)
    limit[name]=[l_limit,r_limit]

def removal_outlier(st,name):
    st = st[st < limit[name][1]]
    st = st[st > limit[name][0]]
    sns.distplot(st, hist=True, kde=True, bins=100, color='red', hist_kws={'edgecolor': 'black'})
    plt.xlabel('Range of ' + str(name))
    plt.title('Histogram + Density for ' + str(name))
    # plt.show()
    plt.savefig('img_dense_no_outliers/' + str(name) + '_clean' + '.png')
    plt.clf()
    plt.cla()


for i in range(2,len(names)):
    IQR_outlier(data[names[i]],names[i])

for i in range(2,len(names)):
    removal_outlier(data[names[i]],names[i])



