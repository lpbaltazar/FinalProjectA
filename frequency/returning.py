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

file = '../sql/query_results/customer_sessioncount_'+str(completion)+'_month.csv'
out = 'results/'+str(completion)+'_MONTH_RETURN_VALUE.csv'
col = 'MONTH'
colname = col+'_RETURN_VALUE'


s = time.time()
df = readChunk(file)
df.rename(columns = {'COUNT(SESSIONID)': 'FREQUENCY'}, inplace = True)
df.FREQUENCY = df.FREQUENCY.astype(int)

new_df = pd.DataFrame(index = df.USERID.unique(), columns = [colname], data = 0)
new_df.index.name = 'USERID'

if col == 'MONTH':
	init = list(df.loc[df.MONTH == '201812'].USERID.unique())
elif col == 'WEEK':
	init = list(df.loc[df.WEEK == '201848'].USERID.unique())

def addvalue(x):
	x = x+1
	print('here')
	return x

df[col] = df[col].astype(float)
for i in df[col].unique():
	print(i)
	if col == 'MONTH':
		if i < 201812: continue
	elif col == 'WEEK':
		if i < 201848: continue

	temp = df.loc[df[col] == i]
	users = list(temp.USERID.unique())
	common = list(set(init).intersection(users))
	# for j in range(len(common)):
	# 	new_df.loc[common[j]][colname] = new_df.loc[common[j]][colname] + 1

	new_df[colname] = new_df.apply(lambda x: addvalue(x[colname]) if str(x.index) in common else x[colname], axis = 1)
	init.extend(users)
	init = list(set(init))

print(new_df.head())
print(new_df[colname].unique())
toCSV(new_df, out, index = False)

e = time.time()
total_time = time.strftime("%H:%M:%S", time.gmtime(e-s))
print("Total time: ", total_time)


