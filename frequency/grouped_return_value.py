import warnings
warnings.filterwarnings('ignore')

import sys
sys.path.append('../')

import os
import time
import pandas as pd
import numpy as np

from utils import readChunk, toCSV

thres = '50'
freq = readChunk("../sql/query_results/customer_sessioncount_"+thres+"_month.csv")
month_return = readChunk("results/"+thres+"_MONTH_RETURN_VALUE.csv")

freq.rename(columns = {'COUNT(SESSIONID)':'FREQUENCY'}, inplace = True)
freq.FREQUENCY = freq.FREQUENCY.astype(int)
freq.MONTH = freq.MONTH.astype(int)
month_return.MONTH_RETURN_VALUE = month_return.MONTH_RETURN_VALUE.astype(int)
freq = freq.loc[freq.MONTH >= 201812]
temp = freq.loc[freq.FREQUENCY == 1]

cols = [0, 1, 2, 3, 4, 5]
df = pd.DataFrame(index = freq.MONTH.unique(), columns = cols)
for i in freq.MONTH.unique():
	temp1 = temp.loc[temp.MONTH == i]
	temp1 = temp1.merge(month_return, how = 'left', on = 'USERID')
	for j in cols:
		df.loc[i][j] = len(temp1.loc[temp1.MONTH_RETURN_VALUE == j])

df.index.name = 'MONTH'
out = "results/"+thres+"/bin1.csv"
toCSV(df, out)


# df1 = pd.read_csv('results/50/bin1.csv')
# df2 = pd.read_csv('results/50/bin2.csv')
# df3 = pd.read_csv('results/50/bin3.csv')
# df4 = pd.read_csv('results/50/bin4.csv')
# df5 = pd.read_csv('results/50/bin5.csv')

def plot_clustered_stacked(dfall, labels=None, title="multiple stacked bar plot",  H="/", **kwargs):
    """Given a list of dataframes, with identical columns and index, create a clustered stacked bar plot. 
labels is a list of the names of the dataframe, used for the legend
title is a string for the title of the plot
H is the hatch used for identification of the different dataframe"""

    n_df = len(dfall)
    n_col = len(dfall[0].columns) 
    n_ind = len(dfall[0].index)
    axe = plt.subplot(111)

    for df in dfall : # for each data frame
        axe = df.plot(kind="bar",
                      linewidth=0,
                      stacked=True,
                      ax=axe,
                      legend=False,
                      grid=False,
                      **kwargs)  # make bar plots

    h,l = axe.get_legend_handles_labels() # get the handles we want to modify
    for i in range(0, n_df * n_col, n_col): # len(h) = n_col * n_df
        for j, pa in enumerate(h[i:i+n_col]):
            for rect in pa.patches: # for each index
                rect.set_x(rect.get_x() + 1 / float(n_df + 1) * i / float(n_col))
                rect.set_hatch(H * int(i / n_col)) #edited part     
                rect.set_width(1 / float(n_df + 1))

    axe.set_xticks((np.arange(0, 2 * n_ind, 2) + 1 / float(n_df + 1)) / 2.)
    axe.set_xticklabels(df.index, rotation = 0)
    axe.set_title(title)

    # Add invisible data to add another legend
    n=[]        
    for i in range(n_df):
        n.append(axe.bar(0, 0, color="gray", hatch=H * i))

    l1 = axe.legend(h[:n_col], l[:n_col], loc=[1.01, 0.5])
    if labels is not None:
        l2 = plt.legend(n, labels, loc=[1.01, 0.1]) 
    axe.add_artist(l1)
    return axe

dfall = [df1, df2, df3, df4, df5]
plot = plot_clustered_stacked(dfall, labels = ['One-time', 'Seldom', 'Occasional', 'Daily', 'Binge'], title = 'Session Frequency and Customer Return Value')