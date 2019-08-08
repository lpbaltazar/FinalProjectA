import warnings
warnings.filterwarnings('ignore')

import sys
sys.path.append('../')

import os
import time
import pandas as pd
import numpy as np

from utils import readChunk, toCSV

thres = '50'

freq = readChunk("../sql/query_results/customer_sessioncount_"+thres+"_month.csv")
month_return = readChunk("results/"+thres+"_MONTH_RETURN_VALUE.csv")

freq.rename(columns = {'COUNT(SESSIONID)':'FREQUENCY'}, inplace = True)
freq.FREQUENCY = freq.FREQUENCY.astype(int)
freq.MONTH = freq.MONTH.astype(int)
month_return.MONTH_RETURN_VALUE = month_return.MONTH_RETURN_VALUE.astype(int)
freq = freq.loc[freq.MONTH >= 201812]
temp = freq.loc[freq.FREQUENCY == 1]

cols = [0, 1, 2, 3, 4, 5]
df = pd.DataFrame(index = freq.MONTH.unique(), columns = cols)
for i in freq.MONTH.unique():
	temp1 = temp.loc[temp.MONTH == i]
	temp1 = temp1.merge(month_return, how = 'left', on = 'USERID')
	for j in cols:
		df.loc[i][j] = len(temp1.loc[temp1.MONTH_RETURN_VALUE == j])

df.index.name = 'MONTH'
toCSV(df, 'results/trial.csv')
