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


df = readChunk('results/50_WEEK_RETURN_VALUE.csv')
df.WEEK_RETURN_VALUE = df.WEEK_RETURN_VALUE.astype(int)
print(df.head())
print(len(df))

tohist = pd.DataFrame(index = df.WEEK_RETURN_VALUE.unique(), columns = ['NUMCUST'])
tohist.index.name = 'MONTH_RETURN_VALUE'
for i in df.WEEK_RETURN_VALUE.unique():
	print(i)
	temp = df.loc[df.WEEK_RETURN_VALUE == i]
	tohist.loc[i]['NUMCUST'] = len(temp)

tohist.sort_index(axis = 0, inplace = True)
plot = tohist.plot(kind = 'bar', colormap = 'Pastel2')
plt.show()