import warnings
warnings.filterwarnings('ignore')

import sys
sys.path.append("../")

import os
import time
import pandas as pd
import numpy as np

from utils import readChunk, toCSV
from matplotlib import pyplot as plt
import seaborn as sns

import matplotlib.style as style

sns.set()
style.use('seaborn-poster')


# df = readChunk('session_information.csv', header = None)
# df.rename(columns  = {0:'USERID', 1:'SESSIONID', 2:'MONTH', 3:'WEEK', 4:'DATE', 5:'STARTHOUR', 6:'ENDHOUR', 7:'TIME_DUR', 8:'WATCHING_DUR', 9:'VID_DUR'}, inplace = True)
# print(df.head())

# cols = ['TIME_DUR', 'WATCHING_DUR', 'VID_DUR']
# for col in cols:
# 	df[col] = pd.to_numeric(df[col], errors = 'coerce')

# tot_time_dur = df.groupby('USERID')['TIME_DUR'].sum().to_frame()
# tot_watch_dur = df.groupby('USERID')['WATCHING_DUR'].sum().to_frame()
# tot_vid_dur = df.groupby('USERID')['VID_DUR'].sum().to_frame()

# new_df = tot_time_dur.merge(tot_watch_dur, how = 'left', on = 'USERID').merge(tot_vid_dur, how = 'left', on = 'USERID')
# new_df['COMPLETION'] = (new_df['WATCHING_DUR']/new_df['VID_DUR'])*100
# toCSV(new_df, 'results/session_duration_vs_completion.csv')

df = readChunk('results/session_duration_vs_completion.csv')
print(df.head())
print(len(df))
cols = ['TIME_DUR', 'WATCHING_DUR', 'VID_DUR', 'COMPLETION']
for col in cols:
	df[col] = pd.to_numeric(df[col], errors = 'coerce')

df.WATCHING_DUR = df.WATCHING_DUR/60.0
df.dropna(subset = cols, inplace = True)
# df = df.loc[df.COMPLETION >= 50.0]
print(df.WATCHING_DUR.min())
print(df.TIME_DUR.min())
q = df.TIME_DUR.quantile(.99)
df = df.loc[df.TIME_DUR <= q]
df = df.loc[df.COMPLETION <= 100]
df = df.loc[df.COMPLETION >= 50]
# plot = sns.regplot(x = 'VID_DUR', y = 'COMPLETION', data = df, fit_reg = False)
# plt.xlabel('TOTAL VIDEO DURATION')
# plt.ylabel('COMPLETION')
# # plot.set_ylim(0,400000)
# plt.show()

def typethres(x):
	if (x >= 0) & (x <= 0.2):
		return 1
	elif (x >= 0.21) & (x <= 0.4):
		return 2
	elif (x >= 0.41) & (x <= 0.6):
		return 3
	elif (x >= 0.61) & (x <= 0.8):
		return 4
	else:
		return 5
df['thresh'] = df.WATCHING_DUR/df.TIME_DUR
df['thresh'] = df.apply(lambda x: typethres(x.thresh), axis = 1)
print(df.thresh)
color = ['red', 'orange', 'yellow', 'green', 'blue']
for j in range(1, 5):
	print(j)
	temp = df.loc[df.thresh == j]
	plot = sns.regplot(x = 'VID_DUR', y = 'WATCHING_DUR', data = temp, fit_reg = False, color = color[j])
# plot = df.plot(kind = 'scatter', x = 'VID_DUR', y = 'WATCHING_DUR', c = 'thresh')
# plot = sns.lmplot(x = 'VID_DUR', y = 'WATCHING_DUR', data = df, hue = 'thresh', fit_reg = False)
plt.show()