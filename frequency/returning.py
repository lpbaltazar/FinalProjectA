import warnings
warnings.filterwarnings('ignore')

import sys
sys.path.append("../")

import os
import time
import pandas as pd
import numpy as np

from utils import readChunk, toCSV

completion = 80

file = 'customer_sessioncount_'+str(completion)+'_month.csv'
out = 'results/'+str(completion)+'_MONTH_RETURN_VALUE.csv'
col = 'MONTH'
colname = col+'_RETURN_VALUE'


df = readChunk(file)
df.rename(columns = {'COUNT(SESSIONID)': 'FREQUENCY'}, inplace = True)
df.FREQUENCY = df.FREQUENCY.astype(int)

new_df = pd.DataFrame(index = df.USERID.unique(), columns = [colname], data = 0)
new_df.index.name = 'USERID'
new_df.reset_index(inplace = True)
print(new_df.columns)

if col == 'MONTH':
	init = list(df.loc[df.MONTH == '201812'].USERID.unique())
elif col == 'WEEK':
	init = list(df.loc[df.WEEK == '201848'].USERID.unique())

def addvalue(x):
	x = x+1
	return x


for i in df[col].unique():
	df[col] = df[col].astype(float)
	if col == 'MONTH]':
		if i < 201812: continue
	elif col == 'WEEK':
		if i < 201848: continue

	temp = df.loc[df[col] == i]
	users = list(temp.USERID.unique())
	common = list(set(init).intersection(users))
	new_df[colname] = new_df.apply(lambda x: addvalue(x.MONTH_RETURN_VALUE) if x.USERID in common else x[colname], axis = 1)
	init.extend(users)
	init = list(set(init))

print(new_df.head())
toCSV(new_df, out, index = False)


