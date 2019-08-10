import warnings
warnings.filterwarnings('ignore')

import sys
sys.path.append("../")

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
# month = '201905'
df = readChunk('../sql/query_results/plateu_all.csv')
df.rename(columns = {'COUNT(SESSIONID)':'FREQUENCY'}, inplace = True)
# df = df.loc[df.MONTH == month]
df.FREQUENCY = df.FREQUENCY.astype(int)
df.COMPLETION = df.COMPLETION.astype(float)
df.dropna(subset = ['COMPLETION'], inplace = True)
print(len(df.loc[df.COMPLETION == 0]))

df = df.loc[df.COMPLETION <= 100]
df = df.loc[df.COMPLETION >= 0]

df = df.loc[df.FREQUENCY <= 200]
print(len(df))
print(df.COMPLETION.mean())
print(df.COMPLETION.median())
plot = sns.regplot(x = 'FREQUENCY', y = 'COMPLETION', data = df, fit_reg = False)
plt.savefig('figures/all.png')



##aa
#/#