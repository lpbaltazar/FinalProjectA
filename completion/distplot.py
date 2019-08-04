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

# df = df.loc[df.COMPLETION >= 70.0]
# print(df.head())
# plot = sns.distplot(df.COMPLETION.values, bins = 20, kde = False)
plot = df.hist(column = 'COMPLETION', bins = [0, 10, 20, 30, 40, 50, 60, 70, 80, 90, 100])
# plot.set(xlabel = 'Percent', ylabel = 'Number of Sessions')
plt.show()