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

# data will be divided into train ( 75% of random data )
train, test = train_test_split(data, test_size=0.25)

print(train)
print(test)