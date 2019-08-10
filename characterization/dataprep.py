import warnings
warnings.filterwarnings("ignore")

import sys
sys.path.append('../')

import os
import time
import pandas as pd
import numpy as np

from utils import readChunk, toCSV

# df = readChunk('session_information.csv', header = None)
# df.rename(columns  = {0:'USERID', 1:'SESSIONID', 2:'MONTH', 3:'WEEK', 4:'DATE', 5:'STARTHOUR', 6:'ENDHOUR', 7:'TIME_DUR', 8:'WATCHING_DUR', 9:'VID_DUR'}, inplace = True)

df = readChunk('dayofweek.csv', header = None)
df.rename(columns = {0:'USERID', 1:'SESSIONID', 2:'DAYOFWEEK'}, inplace = True)
print(df.head())
# df.STARTHOUR = df.STARTHOUR.astype(int)
# print(df.STARTHOUR.unique())

df.DAYOFWEEK = pd.to_numeric(df.DAYOFWEEK, errors = 'coerce')
print(len(df))
df.dropna(subset = ['DAYOFWEEK'], inplace = True)
print(len(df))
print(df.DAYOFWEEK.unique())


time_df = []
tohist = pd.DataFrame(index = list(range(1, 8)), columns = ['COUNT'])
for i in range(1, 8):
	temp = df.loc[df.DAYOFWEEK == i]
	new_df = temp.groupby('USERID')['DAYOFWEEK'].count().to_frame()
	new_df.rename(columns = {'DAYOFWEEK':str(i)}, inplace = True)
	print(new_df.head())
	new_df.fillna(0, inplace = True)
	time_df.append(new_df)
	tohist.loc[i]['COUNT'] = len(temp)

print(len(time_df))
new_df = pd.DataFrame(index = df.USERID.unique())
new_df.index.name = 'USERID'
new_df.reset_index(inplace = True)

for i in range(len(time_df)):
	new_df = new_df.merge(time_df[i], how = 'left', on = 'USERID')

print(new_df.head())
toCSV(new_df, 'DAYOFWEEK.csv')