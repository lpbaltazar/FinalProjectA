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
style.use('bmh')
completion = readChunk("../characterization/completion.csv")
completion.COMPLETION = pd.to_numeric(completion.COMPLETION)
df = readChunk("../characterization/rfe_clustering_5.csv")
df.columns = df.columns.str.upper()
df.FREQUENCY = pd.to_numeric(df.FREQUENCY)
print(len(df))
df = df.merge(completion, how = 'left', on = 'USERID')
print(len(df))

print(len(df.dropna(subset = ['COMPLETION'])))
df.dropna(subset = ['COMPLETION'], inplace = True)
fig, (ax1, ax2, ax3, ax4) = plt.subplots(1, 4, figsize = (48, 18))
temp = df.loc[df.FREQUENCY == 1]
print(len(temp))
bin1 = list(range(0, 110, 10))
fordf = []
# print(len(bin1))
for i in range(len(bin1)):
	if i == 0: continue
	elif i == len(bin1): fordf.append("[{}, {}]".format(bin1[i-1], bin1[i]))
	else: fordf.append("[{}, {})".format(bin1[i-1], bin1[i]))

tohist = pd.DataFrame(index = fordf, columns = ['COUNT'])
for i in range(len(bin1)):
	# print(bin1[i])
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
	ax1.text(i, tohist.iloc[i]['COUNT'], str(tohist.iloc[i]['percent']), horizontalalignment = 'center')

ax1.set_title('ONE TIME USERS')
ax1.title.set_size(30)

temp = df.loc[(df.FREQUENCY >= 2) & (df.FREQUENCY <= 43)]
print(len(temp))
bin1 = list(range(0, 110, 10))
fordf = []
# print(len(bin1))
for i in range(len(bin1)):
	if i == 0: continue
	elif i == len(bin1): fordf.append("[{}, {}]".format(bin1[i-1], bin1[i]))
	else: fordf.append("[{}, {})".format(bin1[i-1], bin1[i]))

tohist = pd.DataFrame(index = fordf, columns = ['COUNT'])
for i in range(len(bin1)):
	# print(bin1[i])
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
	ax2.text(i, tohist.iloc[i]['COUNT'], str(tohist.iloc[i]['percent']), horizontalalignment = 'center')

ax2.set_title('OCCASIONAL USERS')
ax2.title.set_size(30)

temp = df.loc[(df.FREQUENCY >= 44) & (df.FREQUENCY <= 156)]
print(len(temp))
bin1 = list(range(0, 110, 10))
fordf = []
# print(len(bin1))
for i in range(len(bin1)):
	if i == 0: continue
	elif i == len(bin1): fordf.append("[{}, {}]".format(bin1[i-1], bin1[i]))
	else: fordf.append("[{}, {})".format(bin1[i-1], bin1[i]))

tohist = pd.DataFrame(index = fordf, columns = ['COUNT'])
for i in range(len(bin1)):
	# print(bin1[i])
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
	ax3.text(i, tohist.iloc[i]['COUNT'], str(tohist.iloc[i]['percent']), horizontalalignment = 'center')

ax3.set_title('DAILY USERS')
ax3.title.set_size(30)

temp = df.loc[(df.FREQUENCY >= 157)]
print(len(temp))
bin1 = list(range(0, 110, 10))
fordf = []
# print(len(bin1))
for i in range(len(bin1)):
	if i == 0: continue
	elif i == len(bin1): fordf.append("[{}, {}]".format(bin1[i-1], bin1[i]))
	else: fordf.append("[{}, {})".format(bin1[i-1], bin1[i]))

tohist = pd.DataFrame(index = fordf, columns = ['COUNT'])
for i in range(len(bin1)):
	# print(bin1[i])
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
	ax4.text(i, tohist.iloc[i]['COUNT'], str(tohist.iloc[i]['percent']), horizontalalignment = 'center')

ax4.set_title('BINGE USERS')
ax4.title.set_size(30)

# temp = df.loc[(df.FREQUENCY >= 51)]
# print(len(temp))
# bin1 = list(range(0, 110, 10))
# fordf = []
# # print(len(bin1))
# for i in range(len(bin1)):
# 	if i == 0: continue
# 	elif i == len(bin1): fordf.append("[{}, {}]".format(bin1[i-1], bin1[i]))
# 	else: fordf.append("[{}, {})".format(bin1[i-1], bin1[i]))

# tohist = pd.DataFrame(index = fordf, columns = ['COUNT'])
# for i in range(len(bin1)):
# 	# print(bin1[i])
# 	if i == 0: continue
# 	elif i == len(bin1): temp1 = temp.loc[(temp.COMPLETION >= bin1[i-1]) & (temp.COMPLETION <= bin1[i])]
# 	else: temp1 = temp.loc[(temp.COMPLETION >= bin1[i-1]) & (temp.COMPLETION < bin1[i])]

# 	tohist.iloc[i-1]['COUNT'] = len(temp1)

# tot = tohist.COUNT.sum()
# tohist.plot(kind = 'bar', color = 'steelblue', ax = ax5, legend = False)
# tohist['percent'] = (tohist['COUNT']/tot)*100
# tohist['percent'] = tohist['percent'].astype(float)
# tohist['percent'] = round(tohist['percent'], 1)
# for i in range(tohist.shape[0]):
# 	ax5.text(i, tohist.iloc[i]['COUNT'], str(tohist.iloc[i]['percent']), horizontalalignment = 'center')

# ax5.set_title('BINGE USERS')
# ax5.title.set_size(30)
plt.tight_layout()
plt.savefig('figures/frequency_segment_completion_distribution.png', dpi = 300)