import warnings
warnings.filterwarnings('ignore')

import sys
sys.path.append("../")

import os
import time
import pandas as pd
import numpy as np

from utils import readChunk, toCSV

df = readChunk("../sql/query_results/customer_sessioncount_80_month.csv")
df.rename(columns = {'COUNT(SESSIONID)': 'FREQUENCY'}, inplace = True)
df.FREQUENCY = df.FREQUENCY.astype(int)

new_df = pd.DataFrame(index = 'df.USERID.unique()', columns = ['MONTH_RETURN_VALUE'])
new_df.index.name = 'USERID'
new_df.reset_index(inplace = True)

init = list(df.loc[df.MONTH == '201812'].USERID.unique())

def addvalue(x):
	x = x+1
	return x


for month in df.MONTH.unique():
	if month == '201812' | mont == '201811': continue
	temp = df.loc[df.MONTH == month]
	users = list(temp.USERID.unique())
	common = list(set(init).intersection(users))
	new_df['MONTH_RETURN_VALUE'] = new_df.apply(lambda x: addvalue(x.MONTH_RETURN_VALUE) if x.USERID.isin(common) else x.MONTH_RETURN_VALUE)
	init.extend(users)
	init = list(set(init))

print(new_df.head())
toCSV(new_df, '80_MONTH_RETURN_VALUE.csv', index = False)