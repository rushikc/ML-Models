import xlrd
import xlwt
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns  ##used for plotting graphs
import os
## for splitting data into train,test randomly
from sklearn.model_selection import train_test_split
from sklearn import linear_model,datasets



data = pd.read_excel('data.xlsx')
names = data.columns

# data will be divided into train ( 75% of random data )
# train, test = train_test_split(data, test_size=0.25)
lr = linear_model.LinearRegression().fit(X,Y)


exit()


# print(data['AT'])
# data.shape
# data["AT"].plot(kind='hist',bins=100)
# plt.xlabel('AT')
# plt.title('Air data')
# plt.show()
# exit()

for i in range(2,len(names)):
    # data[names[i]].plot(kind='dist',bins=10)

    sns.distplot(data[names[i]], hist=True, kde=True, bins=100, color = 'red',hist_kws={'edgecolor':'black'})
    plt.xlabel('Range of '+str(names[i]))
    plt.title('Histogram + Density for '+str(names[i]))
    # plt.show()
    plt.savefig('img_dense/'+str(names[i])+'.png')
    plt.clf()
    plt.cla()
    # exit()