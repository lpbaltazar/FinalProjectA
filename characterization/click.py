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
for i in cols:
	df[i] = df[i].astype(int)

clusters.LABEL = clusters.LABEL.astype(int)
clusters = clusters.merge(df, how = 'left', on = 'USERID')

for i in clusters.LABEL.unique():
	temp = clusters.loc[clusters.LABEL == i]

	fig, (ax1, ax2, ax3, ax4) = plt.subplots(4)
	sns.distplot(temp.ADPLAY_COUNT.values, color = 'steelblue', ax = ax1)
	ax1.set_title('ADPLAY')
	sns.distplot(temp.PLAY_COUNT.values, color = 'steelblue', ax = ax2)
	ax2.set_title('PLAY')
	sns.distplot(temp.PAUSE_COUNT.values, color = 'steelblue', ax = ax3)
	ax3.set_title('PAUSE')
	sns.distplot(temp.RESUME_COUNT.values, color = 'steelblue', ax = ax4)
	ax4.set_title('RESUME')

	plt.tight_layout()
	plt.show()
	plt.clf()