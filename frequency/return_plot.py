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


df = readChunk('results/50_MONTH_RETURN_VALUE.csv')
print(df.head())


tohist = pd.DataFrame(index = df.MONTH_RETURN_VALUE.unique(), columns = ['NUMCUST'])
tohist.index.name = 'MONTH_RETURN_VALUE'
for i in df.MONTH_RETURN_VALUE:
	temp = df.loc[df.MONTH == i]
	tohist.loc[i]['NUMCUST'] = len(temp)


plot = tohist.plot(kind = 'bar', colormap = 'Pastel2')