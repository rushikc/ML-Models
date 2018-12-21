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

del data['FROM DATE']
del data['TO DATE']

del data['VWS']
del data['TEMP']
del data['AT']
names = data.columns

train = pd.read_excel('dt2_train.xlsx')
test = pd.read_excel('dt2_test.xlsx')
# print(train)


for i in range(len(names)):
    # os.mkdir('scatter_plot/'+names[i])
    for j in range(len(names)):
        if(names[i]!=names[j]):
            train[names[i]] = train[names[i]].apply(np.sqrt)
            train[names[j]] = train[names[j]].apply(np.sqrt)
            test[names[i]] = test[names[i]].apply(np.sqrt)
            test[names[j]] = test[names[j]].apply(np.sqrt)

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

                sns.regplot(y_test, y_pred)
                plt.xlabel(names[i])
                plt.ylabel(names[j])
                plt.title('Scatter plot of ' + str(names[i]) + ' and ' + str(names[j]) + ' ' + str(round(n11)))
                
                plt.savefig('pics2/' + str(names[i]) + '_' + names[j] + '.png')
                plt.clf()
                plt.cla()
