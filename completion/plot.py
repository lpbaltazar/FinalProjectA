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

type_sess = ['total', 'less', '70']
less70 = readChunk("../sql/query_results/month_count_less.csv")
more70 = readChunk("../sql/query_results/month_count_70.csv")

df = more70.merge(less70, on ='MONTH')
df = df.loc[df.MONTH != '201811']
print(df.columns)

df.rename(columns = {'NUMSESSIONS_x': 'COMPLETION_70', 'NUMSESSIONS_y': 'COMPLETION_LESS_THAN_70'}, inplace = True)

print(df.MONTH.unique())
df.COMPLETION_70 = df.COMPLETION_70.astype(float)
df.COMPLETION_LESS_THAN_70 = df.COMPLETION_LESS_THAN_70.astype(float)
df.MONTH = df.MONTH.astype(int)
df['total'] = df.COMPLETION_70 + df.COMPLETION_LESS_THAN_70
df['percent_70'] = round((df.COMPLETION_70/df['total'])*100, 1)
df['percent_less'] = round((df.COMPLETION_LESS_THAN_70/df['total'])*100, 1)
df_deets = df[['MONTH', 'percent_less', 'percent_70', 'total']]
df = df[['MONTH', 'COMPLETION_LESS_THAN_70', 'COMPLETION_70']]

# df['total'] = df.COMPLETION_70 + df.COMPLETION_LESS_THAN_70
# df.COMPLETION_70 = df[['COMPLETION_70', 'total']].apply(lambda x: (x[0]/x[1])*100)
# df.COMPLETION_LESS_THAN_70 = df[['COMPLETION_LESS_THAN_70', 'total']].apply(lambda x: (x[0]/x[1])*100)


df.set_index('MONTH', inplace = True)
df_deets.set_index('MONTH', inplace = True)
plot = df.plot(kind = 'bar', stacked = True, colormap = 'Pastel2')
plot.set_xlabel('MONTH')
plot.set_ylabel('Number of Sessions')

cols = df.index.unique()
for i in range(len(cols)):
	month = cols[i]	
	plot.text(i, df_deets.loc[month]['total'], str(df_deets.loc[month]['total']), fontsize = 6, horizontalalignment = 'center')
	plot.text(i, df.loc[month]['COMPLETION_LESS_THAN_70']/2, str(df_deets.loc[month]['percent_less']), fontsize = 8, horizontalalignment = 'center')
	plot.text(i, (df.loc[month]['COMPLETION_LESS_THAN_70'] + df.loc[month]['COMPLETION_70']/2), str(df_deets.loc[month]['percent_70']), fontsize = 8, horizontalalignment = 'center')
plt.tight_layout()
plt.savefig('figures/num_sessions_completion_month.png')