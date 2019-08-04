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

df = readChunk("../sql/query_results/all_session_completion.csv")
df.dropna(subset = ['COMPLETION'], inplace = True)
print(df.head())
df.COMPLETION = df.COMPLETION.astype(float)

# df = df.loc[df.COMPLETION >= 70.0]
# print(df.head())
# plot = sns.distplot(df.COMPLETION.values, bins = 20, kde = False)
plot = df.hist(column = 'COMPLETION', bins = [0, 10, 20, 30, 40, 50, 60, 70, 80, 90, 100])
# plot.set(xlabel = 'Percent', ylabel = 'Number of Sessions')
plt.savefig('figures/trial1.png')

bin1 = list(range(0, 105, 5))
fordf = []
print(len(bin1))
for i in range(len(bin1)):
	if i == 0: continue
	elif i == 20: fordf.append("[{}, {}]".format(bin1[i-1], bin1[i]))
	else: fordf.append("[{}, {})".format(bin1[i-1], bin1[i]))

tohist = pd.DataFrame(index = fordf, columns = ['COUNT'])
for i in range(len(bin1)):
	if i == 0: continue
	elif i == 20: temp = df.loc[(df.COMPLETION >= bin1[i-1]) & (df.COMPLETION <= bin1[i])]
	else: temp = df.loc[(df.COMPLETION >= bin1[i-1]) & (df.COMPLETION < bin1[i])]

	tohist.iloc[i-1]['COUNT'] = len(temp)


plot = df.plot(kind = 'bar', colormap = 'Pastel2')
plot.set_xlabel('COMPLETION RATE')
plot.set_ylabel('Number of Sessions')
plt.tight_layout()
plt.savefig('figures/trial2.png')