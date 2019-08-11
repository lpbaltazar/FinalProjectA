import warnings
warnings.filterwarnings('ignore')

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
plt.figure(figsize = (5,5))

df = readChunk("../sql/query_results/plateu_all.csv")
df.rename(columns = {'COUNT(SESSIONID)':'FREQUENCY'}, inplace = True)
df.FREQUENCY = df.FREQUENCY.astype(int)
df.COMPLETION = df.COMPLETION.astype(float)
df.dropna(subset = ['COMPLETION'], inplace = True)

fig, (ax1, ax2, ax3, ax4, ax5) = plt.subplots(1, 5)
temp = df.loc[df.FREQUENCY == 1]
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
tohist.plot(kind = 'bar', color = 'steelblue', ax = ax1, legend = False)
tohist['percent'] = (tohist['COUNT']/tot)*100
tohist['percent'] = tohist['percent'].astype(float)
tohist['percent'] = round(tohist['percent'], 1)
for i in range(tohist.shape[0]):
	plot.text(i, tohist.iloc[i]['COUNT'], str(tohist.iloc[i]['percent']), horizontalalignment = 'center')

ax1.set_title('ONE TIME USERS')

temp = df.loc[(df.FREQUENCY >= 2) & (df.FREQUENCY <= 8)]
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
tohist.plot(kind = 'bar', color = 'steelblue', ax = ax2, legend = False)
tohist['percent'] = (tohist['COUNT']/tot)*100
tohist['percent'] = tohist['percent'].astype(float)
tohist['percent'] = round(tohist['percent'], 1)
for i in range(tohist.shape[0]):
	plot.text(i, tohist.iloc[i]['COUNT'], str(tohist.iloc[i]['percent']), horizontalalignment = 'center')

ax2.set_title('SELDOM USERS')

temp = df.loc[(df.FREQUENCY >= 9) & (df.FREQUENCY <= 14)]
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
tohist.plot(kind = 'bar', color = 'steelblue', ax = ax3, legend = False)
tohist['percent'] = (tohist['COUNT']/tot)*100
tohist['percent'] = tohist['percent'].astype(float)
tohist['percent'] = round(tohist['percent'], 1)
for i in range(tohist.shape[0]):
	plot.text(i, tohist.iloc[i]['COUNT'], str(tohist.iloc[i]['percent']), horizontalalignment = 'center')

ax3.set_title('OCCASIONAL USERS')

temp = df.loc[(df.FREQUENCY >= 15) & (df.FREQUENCY <= 50)]
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
tohist.plot(kind = 'bar', color = 'steelblue', ax = ax4, legend = False)
tohist['percent'] = (tohist['COUNT']/tot)*100
tohist['percent'] = tohist['percent'].astype(float)
tohist['percent'] = round(tohist['percent'], 1)
for i in range(tohist.shape[0]):
	plot.text(i, tohist.iloc[i]['COUNT'], str(tohist.iloc[i]['percent']), horizontalalignment = 'center')

ax4.set_title('DAILY USERS')

temp = df.loc[(df.FREQUENCY >= 51)]
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
tohist.plot(kind = 'bar', color = 'steelblue', ax = ax5, legend = False)
tohist['percent'] = (tohist['COUNT']/tot)*100
tohist['percent'] = tohist['percent'].astype(float)
tohist['percent'] = round(tohist['percent'], 1)
for i in range(tohist.shape[0]):
	plot.text(i, tohist.iloc[i]['COUNT'], str(tohist.iloc[i]['percent']), horizontalalignment = 'center')

ax5.set_title('BINGE USERS')
plt.tight_layout()
plt.savefig('figures/bin5_distribution.png')