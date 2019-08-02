import warnings
warnings.filterwarnings("ignore")

import sys
sys.path.append('../')

import os
import time
import pandas as pd
import numpy as np

from utils import readChunk

type_sess = ['total', 'less', '70']
total = readChunk("../sql/query_result/month_count_total.csv")
less70 = readChunk("../sql/query_result/month_count_less.csv")
more70 = readChunk("../sql/query_result/month_count_70.csv")

df = more70.merge(less70, on ='MONTH').merge(total, on = 'MONTH')
print(df.columns)


df['sum'] = df[col1] + df[col2]
df['same'] = df['sum'] - df[col3]
df['same'] = df['same'].apply(lambda x: 0 if x == 0 else 1)
print('Total number of disimalr dates: ', df.same.sum())