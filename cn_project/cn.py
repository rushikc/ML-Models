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


data = pd.read_excel('data.xlsx')


data = data.dropna()

soil = data['soil_type'].values.tolist()
ph = data['ph'].values.tolist()
p = data['av_p'].values.tolist()
k = data['av_k'].values.tolist()
s = data['av_s'].values.tolist()
zn = data['av_zn'].values.tolist()

# limit ={}
# list = []
# for index, row in data.iterrows():
#     st = row['soil_type']
#     if st in list:
#         limit[st]+=1
#     else:
#         list.append(st)
#         limit[st] = 1
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

# print(limit)
# print(soil)


#create new df
# df1 = pd.DataFrame({'col':soil})
# data['soil_type'] = df1

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