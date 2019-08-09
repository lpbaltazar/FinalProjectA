import warnings
warnings.filterwarnings('ignore')

import sys
sys.path.append('ignore')

import os
import time
import pandas as pd
import numpy as np

from utils import readChunk

df = readChunk("../sql/query_results/plateu_all.csv")
df.COMPLETION = df.COMPLETION.astype(float)
df.dropna(subset = ['COMPLETION'], inplace = True)

temp = df.loc[df.COMPLETION <= 80.0]

bin1 = list(range(0, 105, 5))
fordf = []
print(len(bin1))
for i in range(len(bin1)):
	if i == 0: continue
	elif i == 20: fordf.append("[{}, {}]".format(bin1[i-1], bin1[i]))
	else: fordf.append("[{}, {})".format(bin1[i-1], bin1[i]))

tohist = pd.DataFrame(index = fordf, columns = ['COUNT'])
for i in range(len(bin1)):
	if i == 0: continue
	elif i == 20: temp = temp.loc[(temp.COMPLETION >= bin1[i-1]) & (temp.COMPLETION <= bin1[i])]
	else: temp = temp.loc[(temp.COMPLETION >= bin1[i-1]) & (temp.COMPLETION < bin1[i])]

	tohist.iloc[i-1]['COUNT'] = len(temp)

tot = tohist.COUNT.sum()
plot = tohist.plot(kind = 'bar', colormap = 'Pastel2')
tohist['percent'] = (tohist['COUNT']/tot)*100
tohist['percent'] = tohist['percent'].astype(float)
tohist['percent'] = round(tohist['percent'], 1)
# tohist['percent'] = round(tohist['percent'], 1)
for i in range(tohist.shape[0]):
	plot.text(i, tohist.iloc[i]['COUNT'], str(tohist.iloc[i]['percent']), horizontalalignment = 'center')
plot.set_xlabel('COMPLETION RATE')
plot.set_ylabel('NUMBER OF CUSTOMERS')
plt.tight_layout()
plt.savefig('figures/bin1_distribution.png')