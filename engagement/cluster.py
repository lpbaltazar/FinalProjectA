import warnings
warnings.filterwarnings("ignore")

import sys
sys.path.append("../")

import os
import time
import pandas as pd
import numpy as np

from utils import readChunk
from sklearn.cluster import KMeans
from sklearn import metrics

df = readChunk('results/session_duration_vs_completion.csv')
print(df.head())
print(len(df))
cols = ['TIME_DUR', 'WATCHING_DUR', 'COMPLETION']
for col in cols:
	df[col] = pd.to_numeric(df[col], errors = 'coerce')

df.WATCHING_DUR = df.WATCHING_DUR/3600.0
df.TIME_DUR = df.TIME_DUR/60.0
df.dropna(subset = cols, inplace = True)
print(len(df))
df['thresh'] = df.WATCHING_DUR/df.TIME_DUR

clusters = [3,4,5,7]

df = df.loc[(df.thresh <= 1) & (df.thresh >= 0)]
print(len(df))
# for j in range(0,3):
# 	print('Trial:', j)
# 	for i in clusters:
# 		print('Cluster:', i)
# 		km = KMeans(n_clusters = i)
# 		y_km = km.fit_predict(df.thresh.values.reshape(-1,1))
# 		cluster_labels = km.labels_
# 		print(cluster_labels)
# 		sil_score = metrics.silhouette_score(df.thresh.values.reshape(-1,1), cluster_labels, sample_size = 30000)
# 		print(sil_score)


km = KMeans(n_clusters = 3)
y_km = km.fit_predict(df.thresh.values.reshape(-1,1))
df['thresh_LABEL'] = km.labels_
print(df.head())

for i in df.thresh_LABEL.unique():
	temp = df.loc[df.thresh_LABEL == i]
	print(temp.thresh.min())
	print(temp.thresh.max())