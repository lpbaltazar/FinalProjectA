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


df = readChunk("../sql/query_results/all_session_completion.csv")
df.dropna(subset = ['COMPLETION'], inplace = True)
print(df.head())
df.COMPLETION = df.COMPLETION.astype(float)
df['COMPLETION'] = round(df['COMPLETION'], 0)

q3 = df.COMPLETION.quantile(0.75)
q1 = df.COMPLETION.quantile(0.25)
iqr = q3-q1
print('lower limit: {}'.format(q1-(1.5*iqr)))
print('upper limit: {}'.format(q3+(1.5*iqr)))
plot = sns.boxplot(x = 'COMPLETION', data=df, orient = 'v')
plt.savefig('figures/all_session_completion_boxplot.png')