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

sns.set()
style.use('seaborn-poster')

def removeoutlier(df, how = 'iqr'):
	if how == 'iqr':
		q = df.FREQUENCY.quantile(0.75)
		q1 = df.FREQUENCY.quantile(0.25)
		iqr = q-q1
		df = df.loc[(df.FREQUENCY >= q1 - (1.5*iqr)) & (df.FREQUENCY <= q + (1.5*iqr))]
		return df
	elif how == 'zscore':
		mean = df.FREQUENCY.mean()
		std = df.FREQUENCY.std()
		thres = 2
		df["z"] = (np.abs(df.FREQUENCY) - mean)/std
		df = df.loc[df.z < thres]
		df = df[['USERID', 'FREQUENCY']]
		return df


def distPlot(df, xlabel, ylabel, outfile, ylim = None):
	tot = df.COUNT.sum()
	plot = df.plot(kind = 'bar', colormap = 'Pastel2')
	df['percent'] = (df['COUNT']/tot)*100
	df['percent'] = df['percent'].astype(float)
	df['percent'] = round(df['percent'], 1)
	for i in range(tohist.shape[0]):
		plot.text(i, tohist.iloc[i]['COUNT'], str(tohist.iloc[i]['percent']), horizontalalignment = 'center')
	plot.set_xlabel(xlabel)
	plot.set_ylabel(ylabel)
	if ylim:
		plot.set_ylim(0, ylim)
	plt.tight_layout()
	plt.savefig(outfile)
	plt.clf()

def getBins(df, maxi = None, binrange = 2):
	if maxi == None: maxi = max(df.FREQUENCY)
	bin1 = list(range(0, maxi, binrange))
	fordf = []
	for i in range(len(bin1)):
		if i == 0: continue
		elif i == len(df): fordf.append("[{}, {}]".format(bin[i-1], bin1[i]))
		else: fordf.append("[{}, {})".format(bin1[i-1], bin1[i]))

	tohist = pd.DataFrame(index = fordf, columns = ['COUNT'])
	for i in range(len(bin1)):
		if i == 0: continue
		elif i == 20: temp = df.loc[(df.FREQUENCY >= bin1[i-1]) & (df.FREQUENCY <= bin1[i])]
		else: temp = df.loc[(df.FREQUENCY >= bin1[i-1]) & (df.FREQUENCY < bin1[i])]

		tohist.iloc[i-1]['COUNT'] = len(temp)
	return tohist

df = readChunk("../sql/query_results/customer_sessioncount_not_engaaged_month.csv")
df.rename(columns = {'COUNT(SESSIONID)': 'FREQUENCY'}, inplace = True)
df.FREQUENCY = df.FREQUENCY.astype(int)
print(len(df))


df = df.loc[df.MONTH != '201811']
for i in df.MONTH.unique():
	temp = df.loc[df.MONTH == i]
	# temp = removeoutlier(temp)
	# temp = temp.loc[temp.FREQUENCY <= 10]
	xlabel = 'NUMBER OF SESSIONS'
	ylabel = 'NUMBER OF CUSTOMERS'
	outfile = 'figures/month_sessioncount/customer_withoutlier_sessioncount_month_not_engaged'+i+'.png'
	tohist = getBins(temp, binrange = 10, maxi = 200)
	distPlot(tohist, xlabel, ylabel, outfile, ylim = 2)

df = readChunk("../sql/query_results/customer_sessioncount_not_engaged_week.csv")
df.rename(columns = {'COUNT(SESSIONID)': 'FREQUENCY'}, inplace = True)
df.FREQUENCY = df.FREQUENCY.astype(int)
print(len(df))


# df = df.loc[df.MONTH != '201811']
for i in df.WEEK.unique():
	temp = df.loc[df.WEEK == i]
	# temp = removeoutlier(temp)
	# temp = temp.loc[temp.FREQUENCY <= 10]
	xlabel = 'NUMBER OF SESSIONS'
	ylabel = 'NUMBER OF CUSTOMERS'
	outfile = 'figures/week_sessioncount/customer_withoutlier_sessioncount_week_not_engaged'+i+'.png'
	tohist = getBins(temp, binrange = 10, maxi = 100)
	distPlot(tohist, xlabel, ylabel, outfile, ylim = 650000)

