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
style.use('seaborn-talk')



type_sess = ['total', 'less', '70']
less70 = readChunk("../sql/query_result/month_count_less.csv")
more70 = readChunk("../sql/query_result/month_count_70.csv")

df = more70.merge(less70, on ='MONTH')
print(df.columns)

df.rename(columns = {'NUMSESSIONS_X': 'SESSION_70', 'NUMSESSIONS_Y': 'SESSION_LESS'}, inplace = True)

df.SESSION_70 = df.SESSION_70.astype(float)
df.SESSION_LESS = df.SESSION_LESS.astype(float)
df['sum'] = df.SESSION_70 + df.SESSION_LESS
df.SESSION_70 = df[['SESSION_70', 'sum']].apply(lambda x: (x[0]/x[1])*100)
df.SESSION_LESS = df[['SESSION_LESS', 'sum']].apply(lambda x: (x[0]/x[1])*100)



df.set_index('MONTH').T.plot(kind = 'bar', stacked = True)
plt.show()