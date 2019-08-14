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

completion = readChunk('completion.csv')
print(completion.head())
clusters = readChunk('rfe_clustering_5.csv')
clusters.columns = clusters.columns.str.upper()
print(clusters.head())
completion.COMPLETION = completion.COMPLETION.astype(float)
clusters.LABEL = clusters.LABEL.astype(int)
clusters = clusters.merge(completion, how = 'left', on = 'USERID')

for j in clusters.LABEL.unique():
	temp = clusters.loc[clusters.LABEL == j]
	bin1 = list(range(0, 110, 10))
	fordf = []
	print(len(bin1))
	for i in range(len(bin1)):
		if i == 0: continue
		elif i == len(bin1): fordf.append("[{}, {}]".format(bin1[i-1], bin1[i]))
		else: fordf.append("[{}, {})".format(bin1[i-1], bin1[i]))

	tohist = pd.DataFrame(index = fordf, columns = ['COUNT'])
	for i in range(len(bin1)):
		print(bin1[i])
		if i == 0: continue
		elif i == len(bin1): temp1 = temp.loc[(temp.COMPLETION >= bin1[i-1]) & (temp.COMPLETION <= bin1[i])]
		else: temp1 = temp.loc[(temp.COMPLETION >= bin1[i-1]) & (temp.COMPLETION < bin1[i])]

		tohist.iloc[i-1]['COUNT'] = len(temp1)

	tot = tohist.COUNT.sum()
	plot = tohist.plot(kind = 'bar', legend = False, color = 'steelblue')
	tohist['percent'] = (tohist['COUNT']/tot)*100
	tohist['percent'] = tohist['percent'].astype(float)
	tohist['percent'] = round(tohist['percent'], 1)
	for i in range(tohist.shape[0]):
		plot.text(i, tohist.iloc[i]['COUNT'], str(tohist.iloc[i]['percent']), horizontalalignment = 'center')
	plot.set_ylabel('NUMBER OF CUSTOMERS')
	plot.set_xlabel('COMPLETION (%)')
	plt.tight_layout()
	plt.savefig('figures/completion_cluster'+str(j)+'.png')
	plt.clf()