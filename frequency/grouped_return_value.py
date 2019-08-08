import warnings
warnings.filterwarnings('ignore')

import sys
sys.path.append('../')

import os
import time
import pandas as pd
import numpy as np

from utils import readChunk

thres = '50'

freq = readChunk("../sql/query_results/customer_sessioncount_"+thres+"_month.csv")
freq.rename(columns = {'COUNT(SESSIONID':'FREQUENCY'}, inplace = True)
month_return = readChunk("results/"+thres+"_MONTH_RETURN_VALUE.csv")
week_return = readChunk("results/"+thres+"_WEEK_RETURN_VALUE.csv")


freq = freq.merge(month_return, how = 'left', on = 'USERID')
freq = freq.merge(week_return, how = 'left', on = 'USERID')

print(len(freq.loc[freq.MONTH_RETURN_VALUE.isnull()]))
print(len(freq.loc[freq.WEEK_RETURN_VALUE.isnull()]))
freq.FREQUENCY = freq.FREQUENCY.astype(int)
freq.MONTH = freq.MONTH.astype(int)
freq = freq.loc[freq.MONTH > 201811]
freq.WEEK_RETURN_VALUE = freq.WEEK_RETURN_VALUE.astype(int)
freq.MONTH_RETURN_VALUE = freq.MONTH_RETURN_VALUE.astype(int)
temp = freq.loc[freq.FREQUENCY == 1]
cols = [0, 1, 2, 3, 4, 5]
df = pd.DataFrame(index = freq.MONTH.unique(), columns = cols)
for i in freq.MONTH.unique():
	for j in cols:
		df.loc[i][j] = len(temp.loc[temp.MONTH_RETURN_VALUE == j])

df.index.name = 'MONTH'
toCSV(df, 'results/trial.csv')
