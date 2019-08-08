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


completion = '50'
col = 'month'
file = "../sql/query_results/customer_sessioncount_"+completion+"_"+col+".csv"
out = 'figures/customer_sessioncount_'+completion+'_'+col+'_no0-5.png'
col = col.upper()
df = readChunk(file)
df.rename(columns = {'COUNT(SESSIONID)': 'FREQUENCY'}, inplace = True)
df.FREQUENCY = df.FREQUENCY.astype(int)
tohist = []
for i in df[col].unique():
	temp = df.loc[df[col] == i]
	hist = getBins(temp, i, start = 5,  binrange = 5, maxi = 50)
	tohist.append(hist)

tohist = pd.concat(tohist, axis = 1)
# distPlot(tohist, 'NUMBER OF SESSIONS', 'NUMBER OF CUSTOMERS', out, ylim = 60000)


for i in tohist.index.unique():
	temp = tohist.loc[tohist.index == i]
	out = 'figures/customer_sessioncount_'+completion+'_'+col+i+'.csv'
	distPlot(temp, 'NUMBER OF SESSIONS', 'NUMBER OF CUSTOMERS', out)