import warnings
warnings.filterwarnings("ignore")

import sys
sys.path.append("../")

import os
import time
import pandas as pd
import numpy as np

from utils import readChunk

file = "query_results/for_completion_total.csv"
df = readChunk(file)

def countCompletion70(df):
	df.VIDEO_DURATION = df.VIDEO_DURATION.astype(float)
	df.USR_ACT_TOT_WATCHING_DUR = df.USR_ACT_TOT_WATCHING_DUR.astype(float)
	df["completion_70"] = (df.USR_ACT_TOT_WATCHING_DUR/df.VIDEO_DURATION)*100

	print("Total Number of Customers: {}".format(len(df.USERID.unique())))
	df = df.loc[df.completion_70 >= 70]
	print("Total Number of Customers with 70% Completion: {}".format(len(df.USERID.unique())))
	print("\n")

def timeCompletion(df, col):
	for time_comp in df[col].unique():
		print(time_comp)
		temp = df.loc[df[col] == time_comp]
		countCompletion70(temp)

if __name__ == '__main__':
	file = "query_results/for_completion_total.csv"
	df = readChunk(file)
	print("Entire time: ")
	countCompletion70(df)
	file = "query_results/for_completion_monthly.csv"
	df = readChunk(file)
	timeCompletion(df, 'MONTH')
	file = "query_results/for_completion_weekly.csv"
	df = readChunk(file)
	timeCompletion(df, 'WEEK')