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
	df.COMPLETION_70 = df.COMPLETION_70.astype(float)
	print("Total Number of Customers: {}".format(len(df.USERID.unique())))
	df = df.loc[df.completion_70 >= 70]
	print("Total Number of Customers with 70% Completion: {}".format(len(df.USERID.unique())))
	print("\n")
	return df

def timeCompletion(df, col):
	for time_comp in df[col].unique():
		print(time_comp)
		temp = df.loc[df[col] == time_comp]
		countCompletion70(temp)

def getCustomers(df, col = False):
	if col:
		for time_comp in df[col].unique():
			print(time_comp)
			temp = df.loc[df[col] == time_comp]
			temp = completion_70(temp)
			temp = temp[['USERID', 'SESSIONID']]
			toCSV(temp, 'customer70/'+col+'/'+time_comp+'.csv', index = False)

	else:
		temp = countCompletion70(df)
		temp = temp[['USERID', 'SESSIONID']]
		toCSV(temp, 'customer70/customer_completion_70.csv', index = False)


if __name__ == '__main__':
	file = "query_results/for_completion_total.csv"
	df = readChunk(file)
	df.rename(columns = {0:'USERID', 1:'SESSIONID', 2:'MONTH', 3:'WEEK', 4:'DATE', 5:'COMPLETION'}, inplace = True)
	print("Entire time: ")
	countCompletion70(df)
	timeCompletion(df, 'MONTH')
	timeCompletion(df, 'WEEK')