import warnings
warnings.filterwarnings('ignore')

import sys
sys.path.append('../')

import os
import time
import pandas as pd
import numpy as np
import altair as alt

from utils import readChunk, toCSV

# thres = '50'
# freq = readChunk("../sql/query_results/customer_sessioncount_"+thres+"_month.csv")
# month_return = readChunk("results/"+thres+"_MONTH_RETURN_VALUE.csv")

# freq.rename(columns = {'COUNT(SESSIONID)':'FREQUENCY'}, inplace = True)
# freq.FREQUENCY = freq.FREQUENCY.astype(int)
# freq.MONTH = freq.MONTH.astype(int)
# month_return.MONTH_RETURN_VALUE = month_return.MONTH_RETURN_VALUE.astype(int)
# freq = freq.loc[freq.MONTH >= 201812]
# temp = freq.loc[freq.FREQUENCY == 1]

# cols = [0, 1, 2, 3, 4, 5]
# df = pd.DataFrame(index = freq.MONTH.unique(), columns = cols)
# for i in freq.MONTH.unique():
# 	temp1 = temp.loc[temp.MONTH == i]
# 	temp1 = temp1.merge(month_return, how = 'left', on = 'USERID')
# 	for j in cols:
# 		df.loc[i][j] = len(temp1.loc[temp1.MONTH_RETURN_VALUE == j])

# df.index.name = 'MONTH'
# out = "results/"+thres+"/bin1.csv"
# toCSV(df, out)


df1 = pd.read_csv('results/50/bin1.csv')
df2 = pd.read_csv('results/50/bin2.csv')
df3 = pd.read_csv('results/50/bin3.csv')
df4 = pd.read_csv('results/50/bin4.csv')
df5 = pd.read_csv('results/50/bin5.csv')

def prep_df(df, name):
	df.set_index('MONTH', inplace = True)
	df = df.stack().reset_index()
	df.columns = ['c1', 'c2', 'values']
	df['DF'] = name
	return df

df1 = prep_df(df1, 'One-time')
df2 = prep_df(df2, 'Seldom')
df3 = prep_df(df3, 'Occasional')
df4 = prep_df(df4, 'Daily')
df5 = prep_df(df5, 'Binge')

df = pd.concat([df1, df2, df3, df4, df5])

trial = alt.Chart(df).mark_bar().encode(y=alt.Y('values', axis=alt.Axis(grid=False)),
							    x='c2:N', 
							    column=alt.Column('c1:N') ,
							    color='DF:N')
trial.save('trial.png')