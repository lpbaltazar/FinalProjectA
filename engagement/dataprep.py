import warnings
warnings.filterwarnings("ignore")

import sys
sys.path.append("../")

import os
import time
import pandas as pd
import numpy as np

from utils import readChunk, toCSV

df = readChunk("../characterization/session_information.csv", header = None)
df.rename(columns = {0:"USERID", 1:"SESSIONID", 2:"MONTH", 3:"WEEK", 4:"DATE", 5:"START_HOUR", 6:"END_HOUR", 7:"SESISON_DURATION", 8:"WATCHING_DURATION", 9:"VIDEO_DURATION"}, inplace = True)

cols = ["SESSION_DURATION", "WATCHING_DURATION"]
new_df = pd.DataFrame(index = df.USERID.unique())
new_df.index.name = "USERID"
new_df.reset_index()

for i in cols:
	df[i] = pd.to_numeric(df[i], errors = 'coerce')
	new_df = new_df.merge(df.groupby("USERID")[i].sum().to_frame, how = 'left', on = 'USERID')

new_df.WATCHING_DURATION = new_df.WATCHING_DURATION/60.0
new_df['INTERACTION_RATING'] = new_df.WATCHING_DURATION/new_df.SESSION_DURATION
print(new_df.head())

df = readChunk("../characterization/click.csv", header = None)
df.rename(columns = {0:"ADPLAY", 1:"PLAY", 2:"PAUSE", 3:"RESUME", 4:"SEEK"}, inplace = True)
df.drop(columns = ['SEEK'], inplace = True)
cols = ["ADPLAY", "PLAY", "PAUSE", "RESUME"]

for i in cols:
	df[i] = pd.to_numeric(df[i], errors = "coerce")
	new_df = new_df.merge(df[i], how = 'left', on = 'USERID')

print(new_df.head())
df = readChunk("../characterization/seek2.csv")
df.rename(columns = {0:"USERID", 1:"SEEK"}, inplace = True)
df.SEEK = pd.to_numeric(df.SEEK, errors = "coerce")
new_df = new_df.merge(df.SEEK, how = 'left', on = "USERID")

print(new_df.head())
toCSV(new_df, "engagement_attributes.csv", index = False)