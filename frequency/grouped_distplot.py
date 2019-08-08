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

def getBins(df, month, start = 0, maxi = None, binrange = 2):
	if maxi == None: maxi = max(df.FREQUENCY)
	bin1 = list(range(start, maxi, binrange))
	fordf = []
	for i in range(len(bin1)):
		if i == 0: continue
		elif i == len(df): fordf.append("[{}, {}]".format(bin[i-1], bin1[i]))
		else: fordf.append("[{}, {})".format(bin1[i-1], bin1[i]))

	tohist = pd.DataFrame(index = fordf, columns = [month])
	for i in range(len(bin1)):
		if i == 0: continue
		elif i == len(df): temp = df.loc[(df.FREQUENCY >= bin1[i-1]) & (df.FREQUENCY <= bin1[i])]
		else: temp = df.loc[(df.FREQUENCY >= bin1[i-1]) & (df.FREQUENCY < bin1[i])]

		tohist.iloc[i-1][month] = len(temp)
	return tohist

def googleAnalyticsBins(df, col):
	dicts = []
	for i in range(1, 9):
		dicts.append({'bin':str(i), col:len(df.loc[df.FREQUENCY == i])})
	dicts.append({'bin':'9-14', col:len(df.loc[(df.FREQUENCY >= 9) & (df.FREQUENCY <= 14)])})
	dicts.append({'bin':'15-25', col:len(df.loc[(df.FREQUENCY >= 15) & (df.FREQUENCY <= 25)])})
	dicts.append({'bin':'26-50', col:len(df.loc[(df.FREQUENCY >= 26) & (df.FREQUENCY <= 50)])})
	dicts.append({'bin':'51-100', col:len(df.loc[(df.FREQUENCY >= 51) & (df.FREQUENCY <= 100)])})
	dicts.append({'bin':'101-200', col:len(df.loc[(df.FREQUENCY >= 101) & (df.FREQUENCY <= 200)])})
	dicts.append({'bin':'201+', col:len(df.loc[(df.FREQUENCY >= 201)])})
	tohist = pd.DataFrame(dicts)
	tohist.set_index('bin', inplace = True)
	print(tohist.head())
	return(tohist)


def distPlot(df, xlabel, ylabel, outfile, ylim = None):
	# tot = df.COUNT.sum()
	# df = df.transpose()
	plot = df.plot(kind = 'bar', colormap = 'Pastel2')
	plot.set_xlabel(xlabel)
	plot.set_ylabel(ylabel)
	if ylim:
		plot.set_ylim(0, ylim)
	plt.tight_layout()
	plt.savefig(outfile)
	plt.clf()


completion = '80'
col = 'month'
file = "../sql/query_results/customer_sessioncount_"+completion+"_"+col+".csv"
out = 'figures/customer_sessioncount_'+completion+'_'+col+'.png'
col = col.upper()
df = readChunk(file)
df.rename(columns = {'COUNT(SESSIONID)': 'FREQUENCY'}, inplace = True)
df.FREQUENCY = df.FREQUENCY.astype(int)
tohist = []
for i in df[col].unique():
	temp = df.loc[df[col] == i]
	# hist = getBins(temp, i, start = 5,  binrange = 5, maxi = 50)
	hist = googleAnalyticsBins(temp, i)
	tohist.append(hist)

tohist = pd.concat(tohist, axis = 1)
distPlot(tohist, 'NUMBER OF SESSIONS', 'NUMBER OF CUSTOMERS', out)


# for i in tohist.index.unique():
# 	temp = tohist.loc[tohist.index == i]
# 	out = 'figures/customer_sessioncount_'+completion+'_'+col+i+'.png'
# 	distPlot(temp, 'NUMBER OF SESSIONS', 'NUMBER OF CUSTOMERS', out)