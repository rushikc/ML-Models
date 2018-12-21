import xlrd
import xlwt
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns  ##used for plotting graphs
import os
## for splitting data into train,test randomly
from sklearn.model_selection import train_test_split



data = pd.read_excel('data.xlsx')

names = data.columns

# os.mkdir("scatter_plot")
count=0

for i in range(2,len(names)):
    os.mkdir('scatter_plot/'+names[i])
    for j in range(2, len(names)):
        if(names[i]!=names[j]):
            sns.regplot(x=data[names[i]], y=data[names[j]])
            plt.xlabel(names[i])
            plt.ylabel(names[j])
            plt.title('Scatter plot of ' + str(names[i]) + ' and ' + str(names[j]))
            # plt.show()
            # names[j]=names[j].replace(" ","")
            plt.savefig('scatter_plot/' + str(names[i]) + '/' + names[j] + '.png')
            plt.clf()
            count += 1
            plt.cla()

print(count)
            # exit()

