import warnings
warnings.filterwarnings("ignore")

import sys
sys.path.append('../')

import os
import time
import pandas as pd
import numpy as np

from functools import reduce
from utils import readChunk
from matplotlib import pyplot as plt
import seaborn as sns

import matplotlib.style as style

sns.set()
style.use('seaborn-poster')
col = 'WEEK'
limit = 201848
percent_out = 'numsessions_week_percent.csv'
image_out = 'figures/session_distrib_week.png'

df = readChunk("../sql/query_results/numcust_allmonth_80.csv")
# print(df.columns)
# df[col] = df[col].astype(float)
# df = df.loc[df[col] >= limit]
# count_df = pd.DataFrame(index = df[col].unique(), columns = ['80%', '70%', '60%', '50%', 'total'])
# count_df.index.name = col

count_df = df
def getnum(df, count_df, col, limit, colname):
	df.dropna(subset = [col], inplace = True)
	df[col] = df[col].astype(float)
	df = df.loc[df[col] >= limit]
	for i in list(df[col].unique()):
		count_df.loc[i][colname] = len(df.loc[df[col] == i])
	return count_df

def mergesess(df, count_df, col, limit, colname):
	df.NUMSESSIONS = df.NUMSESSIONS.astype(float)
	df.dropna(subset = [col], inplace = True)
	df[col] = df[col].astype(float)
	df = df.loc[df[col] >= limit]
	df.rename(columns = {'NUMSESSIONS': colname}, inplace = True)
	count_df = count_df.merge(df, on = col)
	return count_df


# count_df = getnum(df, count_df, col, limit, '80%')
# df = readChunk("../sql/query_results/numsessions_week_70.csv")
# count_df = getnum(df, count_df, col, limit, '70%')
# df = readChunk("../sql/query_results/numsessions_week_60.csv")
# count_df = getnum(df, count_df, col, limit, '60%')
# df = readChunk("../sql/query_results/numsessions_week_50.csv")
# count_df = getnum(df, count_df, col, limit, '50%')
# df = readChunk("../sql/query_results/numsessions_week_total.csv")
# count_df = getnum(df, count_df, col, limit, 'total')


# count_df = mergesess(df, count_df, col, limit, '80%')
# df = readChunk("../sql/query_results/numsessions_week_70.csv")
# count_df = mergesess(df, count_df, col, limit, '70%')
# df = readChunk("../sql/query_results/numsessions_week_60.csv")
# count_df = mergesess(df, count_df, col, limit, '60%')
# df = readChunk("../sql/query_results/numsessions_week_50.csv")
# count_df = mergesess(df, count_df, col, limit, '50%')
# df = readChunk("../sql/query_results/numsessions_week_total.csv")
# count_df = mergesess(df, count_df, col, limit, 'total')


print(len(df))
df = readChunk("../sql/query_results/numcust_allmonth_70.csv")
print(len(df))
df = readChunk("../sql/query_results/numcust_allmonth_60.csv")
print(len(df))
df = readChunk("../sql/query_results/numcust_allmonth_50.csv")
print(len(df))
df = readChunk("../sql/query_results/numcust_allmonth_total.csv")
print(len(df))

# print(count_df.head())
# count_df.set_index(col, inplace = True)
# count_df.index = count_df.index.astype(int)
# numsessions_week = count_df[['80%', '70%', '60%', '50%']]
# count_df['percent_80'] = (count_df['80%']/count_df['total'])*100
# count_df['percent_70'] = (count_df['70%']/count_df['total'])*100
# count_df['percent_60'] = (count_df['60%']/count_df['total'])*100
# count_df['percent_50'] = (count_df['50%']/count_df['total'])*100
# percent = count_df[['percent_80', 'percent_70', 'percent_60', 'percent_50']]
# percent.to_csv(percent_out, index = True)
# plot = numsessions_week.plot(kind = 'bar', colormap = 'Pastel2')
# cols = numsessions_week.columns
# cols2 = percent.columns
# plot.set_xlabel(col)
# plot.set_ylabel('NUMBER OF SESSIONS')
# plt.tight_layout()
# plt.savefig(image_out)
