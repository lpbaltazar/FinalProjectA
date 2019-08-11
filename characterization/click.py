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

fig, (ax1, ax2, ax3, ax4) = plt.subplots(4)
ax1 = sns.distplot(df.ADPLAY_COUNT.values, color = 'steelblue')
ax1.set_title('ADPLAY')
ax2 = sns.distplot(df.PLAY_COUNT.values, color = 'steelblue')
ax2.set_title('PLAY')
ax3 = sns.distplot(df.PAUSE_COUNT.values, color = 'steelblue')
ax3.set_title('PAUSE')
ax4 = sns.distplot(df.RESUME_COUNT.values, color = 'steelblue')
ax4.set_title('RESUME')

plt.show()