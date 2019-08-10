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

start = readChunk('DAYOFWEEK.csv')
print(start.head())
clusters = readChunk('rfe_clustering_5.csv')
clusters.columns = clusters.columns.str.upper()
print(clusters.head())

for i in range(1, 8):
	start[str(i)] = pd.to_numeric(start[str(i)], errors = 'coerce')
clusters.LABEL = clusters.LABEL.astype(int)
clusters = clusters.merge(start, how = 'left', on = 'USERID')

def tobin(df):
	tohist = pd.DataFrame(index = list(range(1, 8)), columns = ['COUNT'])
	tohist.index.name = 'DAY'
	print(len(df))
	for i in range(1, 8):
		# tohist.loc[i]['COUNT'] = len(df.dropna(subset = [str(i)]))
		tohist.loc[i]['COUNT'] = df[str(i)].sum()
	print(tohist.head())
	tohist.reset_index(inplace = True)
	return(tohist)

for i in clusters.LABEL.unique():
	temp = clusters.loc[clusters.LABEL == i]
	tohist = tobin(temp)
	plot = sns.barplot(x = 'DAY', y = 'COUNT', data = tohist, color = 'blue', saturation = 0.5)
	plot.set_xlabel('NUMBER OF SESSIONS')
	plot.set_ylabel('DAY OF THE WEEK')
	plot.set(xticklabels = ['SUNDAY', 'MONDAY', 'TUESDAY', 'WEDNESDAY', 'THURSDAY', 'FRIDAY', 'SATURDAY'])
	# plot.set_ylim(0, 2000000)
	plt.savefig('figures/week_number_sessions_cluster'+str(i)+'.png')
	plt.clf()