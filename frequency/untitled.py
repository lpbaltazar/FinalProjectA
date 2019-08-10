import sys
sys.path.append("../")

import pandas as pd
import numpy as np

from utils import readChunk, toCSV

df = readChunk("../../events/MONTH_SESSION_TIME_CATEGORY_WITH_TIME_DURATION.csv", header = None)

df.rename(columns = {0:'MONTH', 1:'USERID', 2:'SESSIONID', 3:'STARTHOUR', 4:'ENDHOUR', 5:'engagement'}, inplace = True)
print(df.head())
df.engagement = df.engagement.astype(float)
df.MONTH = df.MONTH.astype(int)
df = df.loc[df.MONTH >= 201812]

total_df = df.groupby('USERID')['engagement'].sum().to_frame()
total_df.engagement = total_df.engagement/60.0
print(total_df.head())
toCSV(total_df, 'results/overall_engagement.csv')