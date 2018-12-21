import xlrd
import xlwt
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import os

data = pd.read_excel('data.xlsx')

data.corr()

names = data.columns

data.drop_duplicates(inplace=True)  # removing duplicates

data = data.dropna(how='any')

writer=pd.ExcelWriter('data_nona.xlsx')
data.to_excel(writer,'Sheet1')
writer.save()

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

soil = data['soil_type'].values.tolist()
ph = data['ph'].values.tolist()
p = data['av_p'].values.tolist()
k = data['av_k'].values.tolist()
s = data['av_s'].values.tolist()
zn = data['av_zn'].values.tolist()


from scipy.stats import zscore

data.apply(zscore)  # feature scaling

data = (data - data.min()) / (data.max() - data.min()) #min-max normalization

from sklearn.model_selection import train_test_split

train, test = train_test_split(data, test_size=0.25)  # splitting data

limit={}
limit['RED SANDY']=1
limit['BLACK SOIL']=1
limit['SANDY SOIL']=1
limit['others']=1
limit['RED SOIL']=1

for i in range(soil.__len__()):
    st = str(soil[i]).upper()
    if st.__contains__('RED SANDY'):
        limit[st]+=1
    elif st.__contains__('RED SOIL'):
        limit[st]+=1
    elif st.__contains__('BLACK SOIL'):
        limit[st] += 1
    elif st.__contains__('SANDY SOIL') or st.__contains__('SANDY LOAM'):
        limit['SANDY SOIL'] += 1
    else:
        soil[i] = 'others'
        limit['others']+=1

df = pd.DataFrame()
for column in data.columns[10:]:
    df[column] = data[column]


df1 = pd.DataFrame({'col':soil})
df['soil'] = df1


del df['authority']
del df['av_b']
del df['av_fe']
del df['av_cu']
del df['av_mn']

df.dropna()

df.to_excel('data1.xlsx')