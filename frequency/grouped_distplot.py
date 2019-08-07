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

def getBins(df, month, maxi = None, binrange = 2):
	if maxi == None: maxi = max(df.FREQUENCY)
	bin1 = list(range(0, maxi, binrange))
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
	tot = df.COUNT.sum()
	plot = df.plot(kind = 'bar', colormap = 'Pastel2')
	plot.set_xlabel(xlabel)
	plot.set_ylabel(ylabel)
	if ylim:
		plot.set_ylim(0, ylim)
	plt.tight_layout()
	plt.savefig(outfile)
	plt.clf()


df = readChunk("../sql/query_results/customer_sessioncount_80_week.csv")
df.rename(columns = {'COUNT(SESSIONID)': 'FREQUENCY'}, inplace = True)
df.FREQUENCY = df.FREQUENCY.astype(int)
tohist = []
for i in df.MONTH.unique():
	temp = df.loc[df.MONTH == i]
	hist = getBins(temp, binrange = 10, maxi = 200)
	tohist.append(hist)

tohist = pd.concat(tohist, axis = 1)
print(tohist.head())