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
less70 = readChunk("../sql/query_results/date_count_less.csv")
more70 = readChunk("../sql/query_results/date_count_70.csv")

df = more70.merge(less70, on ='DATE')
print(df.columns)

df.rename(columns = {'NUMSESSIONS_x': 'COMPLETION_70', 'NUMSESSIONS_y': 'COMPLETION_LESS_THAN_70'}, inplace = True)

print(df.DATE.unique())
df.COMPLETION_70 = df.COMPLETION_70.astype(float)
df.COMPLETION_LESS_THAN_70 = df.COMPLETION_LESS_THAN_70.astype(float)
df['DATE'] = df['DATE'].to_datetime()
df['total'] = df.COMPLETION_70 + df.COMPLETION_LESS_THAN_70
df['percent_70'] = round((df.COMPLETION_70/df['total'])*100, 1)
df['percent_less'] = round((df.COMPLETION_LESS_THAN_70/df['total'])*100, 1)
df_deets = df[['DATE', 'percent_less', 'percent_70', 'total']]
df = df[['DATE', 'COMPLETION_LESS_THAN_70', 'COMPLETION_70']]

# df['total'] = df.COMPLETION_70 + df.COMPLETION_LESS_THAN_70
# df.COMPLETION_70 = df[['COMPLETION_70', 'total']].apply(lambda x: (x[0]/x[1])*100)
# df.COMPLETION_LESS_THAN_70 = df[['COMPLETION_LESS_THAN_70', 'total']].apply(lambda x: (x[0]/x[1])*100)


# df.set_index('DATE', inplace = True)
df_deets.set_index('DATE', inplace = True)
plot = df.plot(x = 'DATE', y = 'percent_70', data = df, kind = 'line', colormap = 'Pastel2')
plot.set_xlabel('DATE')
plot.set_ylabel('NUMBER OF CUSTOMERS')

plt.tight_layout()
plt.savefig('figures/num_cust_completion_daily.png')