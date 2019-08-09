import sys
sys.path("../")

import pandas as pd
import numpy as np

from utils import readChunk, toCSV

df = readChunk("../../events/MONTH_SESSION_TIME_CATEGORY_DURATION.csv")

df.rename(columns = {0:'MONTH', 1:'USERID', 2:'SESSIONID', 3:'STARTHOUR', 4:'ENDHOUR', 5:'SESSIONDURATION'}, inplace = True)
df.SESSIONDURATION = df.SESSIONDURATION.astype(float)
df.MONTH = df.MONTH.astype(int)
df = df.loc[df.MONTH >= 201812]

total_df = df.groupby('USERID')['SESSIONDURATION'].sum().to_frame()
print(total_df.head())
toCSV(total_df, 'results/overall_engagement.csv')