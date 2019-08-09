import warnings
warnings.filterwarnings('ignore')

import sys
sys.path.append("../")

import os
import time
import pandas as pd
import numpy as np

from utils import readChunk, toCSV


df = readChunk('session_information.csv', header = None)
df.rename(columns  = {0:'USERID', 1:'SESSIONID', 2:'MONTH', 3:'WEEK', 4:'DATE', 5:'STARTHOUR', 6:'ENDHOUR', 7:'TIME_DUR', 8:'WATCHING_DUR', 9:'VID_DUR'}, inplace = True)
print(df.head())

cols = ['TIME_DUR', 'WATCHING_DUR', 'VID_DUR']
for col in cols:
	df[col] = pd.to_numeric(df[col], errors = 'coerce')

tot_time_dur = df.groupby('USERID')['TIME_DUR'].sum().to_frame()
tot_watch_dur = df.groupby('USERID')['WATCHING_DUR'].sum().to_frame()
tot_vid_dur = df.groupby('USERID')['VID_DUR'].sum().to_frame()

new_df = tot_time_dur.merge(tot_watch_dur, how = 'left', on = 'USERID').merge(tot_vid_dur, how = 'left', on = 'USERID')
new_df['COMPLETION'] = (new_df['WATCHING_DUR']/new_df['VID_DUR'])*100
toCSV(new_df, 'results/session_duration_vs_completion.csv')

