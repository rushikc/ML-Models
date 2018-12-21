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




data = pd.read_excel('data_zscore.xlsx')





from sklearn.model_selection import train_test_split

train, test = train_test_split(data, test_size=0.25)

train.to_excel('train_zscore.xlsx')
test.to_excel('test_zscore.xlsx')

