import warnings
warnings.filterwarnings("ignore")

import sys
sys.path.append("../")

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
style.use('bmh')

start = readChunk('STARTHOUR.csv')
print(start.head())
clusters = readChunk('rfe_clustering_5.csv')
clusters.columns = clusters.columns.str.upper()
print(clusters.head())

for i in range(0, 24):
	start[str(i)] = pd.to_numeric(start[str(i)], errors = 'coerce')
clusters.LABEL = clusters.LABEL.astype(int)
clusters = clusters.merge(start, how = 'left', on = 'USERID')

def tobin(df):
	tohist = pd.DataFrame(index = list(range(0,24)), columns = ['COUNT'])
	tohist.index.name = 'HOUR'
	print(len(df))
	for i in range(0, 24):
		# tohist.loc[i]['COUNT'] = len(df.dropna(subset = [str(i)]))
		tohist.loc[i]['COUNT'] = df[str(i)].sum()
	print(tohist.head())
	tohist.reset_index(inplace = True)
	return(tohist)

for i in clusters.LABEL.unique():
	temp = clusters.loc[clusters.LABEL == i]
	tohist = tobin(temp)
	plot = sns.barplot(x = 'HOUR', y = 'COUNT', data = tohist, color = 'steelblue')
	plot.set_ylabel('NUMBER OF SESSIONS')
	plot.set_xlabel('HOUR OF THE DAY')
	# plot.set_ylim(0, 2000000)
	plt.savefig('figures/number_sessions_cluster'+str(i)+'.png')
	plt.clf()

temp = clusters
tohist = tobin(temp)
plot = sns.barplot(x = 'HOUR', y = 'COUNT', data = tohist, color = 'steelblue')
plot.set_ylabel('NUMBER OF SESSIONS')
plot.set_xlabel('HOUR OF THE DAY')
# plot.set_ylim(0, 2000000)
plt.savefig('figures/number_sessions_cluster.png')
plt.clf()