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

df = readChunk('CLICK.csv')
cols = ['ADPLAY_COUNT', 'PLAY_COUNT', 'PAUSE_COUNT', 'RESUME_COUNT']
clusters = readChunk('rfe_clustering_5.csv')
clusters.columns = clusters.columns.str.upper()
print(clusters.head())
for i in cols:
	df[i] = df[i].astype(int)

clusters.LABEL = clusters.LABEL.astype(int)
clusters = clusters.merge(df, how = 'left', on = 'USERID')

for i in clusters.LABEL.unique():
	temp = clusters.loc[clusters.LABEL == i]
	q = temp.ADPLAY_COUNT.quantile(0.99)
	temp1 = temp.loc[temp.ADPLAY_COUNT <= q]

	q = temp.PLAY_COUNT.quantile(0.99)
	temp2 = temp.loc[temp.ADPLAY_COUNT <= q]

	q = temp.PAUSE_COUNT.quantile(0.99)
	temp3 = temp.loc[temp.ADPLAY_COUNT <= q]

	q = temp.RESUME.quantile(0.99)
	temp4 = temp.loc[temp.ADPLAY_COUNT <= q]

	fig, (ax1, ax2, ax3, ax4) = plt.subplots(4)
	sns.distplot(temp1.ADPLAY_COUNT.values, color = 'steelblue', ax = ax1)
	ax1.set_title('ADPLAY')
	sns.distplot(temp2.PLAY_COUNT.values, color = 'steelblue', ax = ax2)
	ax2.set_title('PLAY')
	sns.distplot(temp3.PAUSE_COUNT.values, color = 'steelblue', ax = ax3)
	ax3.set_title('PAUSE')
	sns.distplot(temp4.RESUME_COUNT.values, color = 'steelblue', ax = ax4)
	ax4.set_title('RESUME')

	plt.tight_layout()
	plt.savefig('figures/click_cluster'+str(i)+'.png')
	plt.clf()