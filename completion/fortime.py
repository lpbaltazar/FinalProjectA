import warnings
warnings.filterwarnings("ignore")

import sys
sys.path.append('../')

import os
import time
import pandas as pd
import numpy as np

from utils import readChunk
from matplotlib import pyplot as plt
import seaborn as sns

import matplotlib.style as style
from statsmodels.tsa.stattools import adfuller


sns.set()
style.use('seaborn-poster')

type_sess = ['total', 'less', '70']
less70 = readChunk("../sql/query_results/date_count_50_less.csv")
more70 = readChunk("../sql/query_results/date_count_50.csv")

df = more70.merge(less70, on ='DATE')
print(df.columns)

df.rename(columns = {'NUMSESSIONS_x': 'COMPLETION_70', 'NUMSESSIONS_y': 'COMPLETION_LESS_THAN_70'}, inplace = True)

print(df.DATE.unique())
df.COMPLETION_70 = df.COMPLETION_70.astype(float)
df.COMPLETION_LESS_THAN_70 = df.COMPLETION_LESS_THAN_70.astype(float)
df['DATE'] = pd.to_datetime(df['DATE'])
df['total'] = df.COMPLETION_70 + df.COMPLETION_LESS_THAN_70
df['percent_70'] = round((df.COMPLETION_70/df['total'])*100, 1)
df['percent_less'] = round((df.COMPLETION_LESS_THAN_70/df['total'])*100, 1)
df_deets = df[['DATE', 'percent_less', 'percent_70', 'total']]
df = df[['DATE', 'COMPLETION_LESS_THAN_70', 'COMPLETION_70']]

# df['total'] = df.COMPLETION_70 + df.COMPLETION_LESS_THAN_70
# df.COMPLETION_70 = df[['COMPLETION_70', 'total']].apply(lambda x: (x[0]/x[1])*100)
# df.COMPLETION_LESS_THAN_70 = df[['COMPLETION_LESS_THAN_70', 'total']].apply(lambda x: (x[0]/x[1])*100)


# df.set_index('DATE', inplace = True)
# df.set_index('DATE', inplace = True)
# plot = df.plot(x = 'DATE', y = 'COMPLETION_70', kind = 'bar', colormap = 'Pastel2', legend = False)
# plot.set_xlabel('DATE')
# plot.set_ylabel('NUMBER OF CUSTOMERS')

# plt.tight_layout()
# plt.savefig('figures/num_cust_completion_daily_bar.png')

def adftest(X):
	result = adfuller(X)
	print('ADF Statistic: %f' % result[0])
	print('p-value: %f' % result[1])
	print('Critical Values: ')
	for key, value in result[4].items():
		print('\t%s: %.3f' % (key, value))


def test_stationary(df):
	X = df.COMPLETION_70.values
	adftest(X)
	df = df[['DATE', 'COMPLETION_70']]
	df.set_index('DATE', inplace = True)
	rolmean = df.rolling(7).mean()
	rolstd = df.rolling(7).std()
	plt.set_cmap('Pastel2')
	orig = plt.plot(df, label = 'Original')
	mean = plt.plot(rolmean, label = 'Rolling Mean')
	std = plt.plot(rolstd, label = 'Rolling Std')
	plt.legend(loc = 'best')
	plt.title('Rolling Mean and Standarad Deviation')
	plt.savefig('figures/rolling_mean_std_50.png')

test_stationary(df)