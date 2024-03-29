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
cols = ['ADPLAY_COUNT', 'PLAY_COUNT', 'PAUSE_COUNT', 'RESUME_COUNT', 'SEEK_COUNT']
clusters = readChunk('rfe_clustering_5.csv')
clusters.columns = clusters.columns.str.upper()
print(clusters.head())
for i in cols:
	df[i] = df[i].astype(int)

clusters.LABEL = clusters.LABEL.astype(int)
clusters.FREQUENCY = clusters.FREQUENCY.astype(float)
clusters = clusters.merge(df, how = 'left', on = 'USERID')


for i in clusters.LABEL.unique():
	temp = clusters.loc[clusters.LABEL == i]
	print(i)
	print(len(temp))
	tot = temp.ADPLAY_COUNT.sum() + temp.PLAY_COUNT.sum() + temp.PAUSE_COUNT.sum() + temp.RESUME_COUNT.sum() + temp.SEEK_COUNT.sum()
	print('Adplay: ', temp.ADPLAY_COUNT.sum()/tot)
	print('Play: ', temp.PLAY_COUNT.sum()/tot)
	print('Pause: ', temp.PAUSE_COUNT.sum()/tot)
	print('Resume: ', temp.RESUME_COUNT.sum()/tot)
	print('Seek: ', temp.SEEK_COUNT.sum()/tot)
	print('Total Frequency: ', temp.FREQUENCY.sum()/clusters.FREQUENCY.sum())
	q = temp.ADPLAY_COUNT.quantile(0.90)
	temp1 = temp.loc[temp.ADPLAY_COUNT <= q]

	q = temp.PLAY_COUNT.quantile(0.90)
	temp2 = temp.loc[temp.PLAY_COUNT <= q]

	q = temp.PAUSE_COUNT.quantile(0.90)
	temp3 = temp.loc[temp.PAUSE_COUNT <= q]

	q = temp.RESUME_COUNT.quantile(0.90)
	temp4 = temp.loc[temp.RESUME_COUNT <= q]

	q = temp.SEEK_COUNT.quantile(0.90)
	temp5 = temp.loc[temp.SEEK_COUNT <= q]

	fig, (ax1, ax2, ax3, ax4, ax5) = plt.subplots(5)
	sns.distplot(temp1.ADPLAY_COUNT.values, color = 'steelblue', ax = ax1)
	ax1.set_title('ADPLAY')
	sns.distplot(temp2.PLAY_COUNT.values, color = 'steelblue', ax = ax2)
	ax2.set_title('PLAY')
	sns.distplot(temp3.PAUSE_COUNT.values, color = 'steelblue', ax = ax3)
	ax3.set_title('PAUSE')
	sns.distplot(temp4.RESUME_COUNT.values, color = 'steelblue', ax = ax4)
	ax4.set_title('RESUME')
	sns.distplot(temp5.SEEK_COUNT.values, color = 'steelblue', ax = ax5)
	ax5.set_title('SEEK')

	plt.tight_layout()
	# plt.savefig('figures/click_cluster'+str(i)+'.png')
	# plt.show()
	plt.clf()