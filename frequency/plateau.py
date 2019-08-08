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

df = readChunk('../sql/query_results/plateu_all.csv')
df.rename(columns = {'COUNT(SESSIONID)':'FREQUENCY'}, inplace = True)

df.FREQUENCY = df.FREQUENCY.astype(int)
df.COMPLETION = df.COMPLETION.astype(float)
plot = sns.regplot(x = 'FREQUENCY', y = 'COMPLETION', data = df, scatter = True, fit_reg = False)
plt.show()
