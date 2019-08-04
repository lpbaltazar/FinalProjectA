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

df = readChunk("../sql/query_results/all_average_completion.csv")
tot = len(df)
df.rename(columns = {'AVGCOMPLETION':'COMPLETION'}, inplace = True)
df.dropna(subset = ['COMPLETION'], inplace = True)
print('Total number of customers: ', tot)
print('Removed customers: ', tot-len(df))
print(df.head())
df.COMPLETION = df.COMPLETION.astype(float)

# df = df.loc[df.COMPLETION >= 70.0]
# print(df.head())
# plot = sns.distplot(df.COMPLETION.values, bins = 20, kde = False)
# plot = df.hist(column = 'COMPLETION', bins = [0, 5, 10, 15, 20, 25, 30, 35, 40, 45, 50, 55, 60, 65, 70, 75, 80, 85, 90, 95, 100])
# plot.set(xlabel = 'Percent', ylabel = 'Number of Sessions')
# plt.savefig('figures/trial1.png')

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

tot = tohist.COUNT.sum()
plot = tohist.plot(kind = 'bar', colormap = 'Pastel2')
tohist['percent'] = (tohist['COUNT']/tot)*100
tohist['percent'] = tohist['percent'].astype(float)
tohist['percent'] = round(tohist['percent'], 1)
# tohist['percent'] = round(tohist['percent'], 1)
for i in range(tohist.shape[0]):
	plot.text(i, tohist.iloc[i]['COUNT'], str(tohist.iloc[i]['percent']), horizontalalignment = 'center')
plot.set_xlabel('COMPLETION RATE')
plot.set_ylabel('NUMBER OF CUSTOMERS')
plt.tight_layout()
plt.savefig('figures/customer_average_completion.png')