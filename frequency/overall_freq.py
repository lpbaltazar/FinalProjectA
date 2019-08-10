import sys
sys.path.append("../")

import pandas as pd
import numpy as np

from utils import readChunk, toCSV

df = readChunk("../sql/query_results/plateu_month.csv")

df.rename(columns = {'COUNT(SESSIONID)':'FREQUENCY'}, inplace = True)
df.FREQUENCY = df.FREQUENCY.astype(int)
df.MONTH = df.MONTH.astype(int)
df = df.loc[df.MONTH >= 201812]
total_df = pd.DataFrame(index = df.index.unique(), columns = ['frequency'])

total_df = df.groupby('USERID')['FREQUENCY'].sum().to_frame()

# for i in df.MONTH.unique():
# 	print(i)
# 	temp = df.loc[df.MONTH == i]
# 	users = temp.index.unique()
# 	for j in users:
# 		total_df.loc[j]['frequency'] = total_df.loc[j]['frequency'] + temp.loc[j]['FREQUENCY']

print(total_df.head())
total_df.index.name = 'USERID'
toCSV(total_df, 'results/overall_frequency.csv')