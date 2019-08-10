import warnings
warnings.filterwarnings("ignore")

import sys
sys.path..append("../")

import os
import time
import pandas as pd
import numpy as np

from utils readChunk
from matplotlib import pyplot as plt
import seaborn as sns

import matplotlib.style as style

sns.set()
style.use('seaborn-poster')

start = readChunk('STARTHOUR.csv')
clusters = readChunk('rfe_clustering_5.csv')

for i in range(0, 24):
	start[i] = start[i].astype(int)
clusters = clusters.merge(start, how = 'left', on = 'USERID')

def tobin(df):
	tohist = pd.DataFrame(index = list(range(0,24)), column = 'COUNT')
	tohist.index.name = 'HOUR'
	for i in range(0, 24):
		tohist.loc[i]['COUNT'] = len(df.loc[df[col] != 0])
	print(tohist.head())
	tohist.reset_index(inplace = True)
	return(tohist)

for i in clusters.label.unique():
	temp = clusters.loc[clusters.label == i]
	tohist = tobin(temp)
	plot = sns.barplot(x = 'HOUR', y = 'COUNT', data = tohist, legend = False)
	plot.set_xlabel('NUMBER OF CUSTOMERS')
	plot.set_ylabel('HOUR OF THE DAY')
	plt.show()