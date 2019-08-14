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

df = readChunk("../characterization/rfe_clustering_5.csv")
df.columns = df.columns.str.upper()
df.FREQUENCY = pd.to_numeric(df.FREQUENCY)

clusters = [3,5,7]

df = df.loc[df.FREQUENCY > 1]
# for j in range(0,3):
# 	print('Trial:', j)
# 	for i in clusters:
# 		print('Cluster:', i)
# 		km = KMeans(n_clusters = i)
# 		y_km = km.fit_predict(df.FREQUENCY.values.reshape(-1,1))
# 		cluster_labels = km.labels_
# 		print(cluster_labels)
# 		sil_score = metrics.silhouette_score(df.FREQUENCY.values.reshape(-1,1), cluster_labels, sample_size = 30000)
# 		print(sil_score)


km = KMeans(n_clusters = 3)
y_km = km.fit_predict(df.FREQUENCY.values.reshape(-1,1))
df['FREQ_LAABEL'] = km.labels_
print(df.head())

for i in df.FREQ_LAABEL.unique():
	temp = df.loc[df.FREQ_LAABEL == i]
	print(temp.FREQUENCY.min())
	print(temp.FREQUENCY.max())