import warnings
warnings.filterwarnings('ignore')

import sys
sys.path.append('../')

import os
import time
import pandas as pandas
import pymysql.cursors

from utils import toCSV

def main(cursor, query, outfile):
	
	s = time.time()
	df = pd.read_sql(query, con = cursor, chunksize = 5000000)
	df = pd.concat(df)
	print(df.head())
	toCSV(df, outfile, index = False)
	e = time.time()
	total_time = time.strftime("%H:%M:%S", time.gmtime(e-s))
	print("Total query time: ", total_time)


if __name__ == '__main__':
	cursor = pymysql.connect(host = "localhost", user = 'rigi', password = 'pwd@rigi', db = 'events_db')
	query = '''SELECT USERID, SESSIONID, VIDEO_DURATION, USR_ACT_TOT_WATCHING_DUR FROM events_data
			'''
	outfile = "query_results/for_completion_total.csv"
	main(query, outfile)
	query = '''SELECT EXTRACT(YEAR_MONTH FROM SESSION_STARTDT) AS MONTH, USERID, SESSIONID, VIDEO_DURATION, USR_ACT_TOT_WATCHING_DUR FROM events_data GROUP BY EXTRACT(YEAR_MONTH FROM SESSION_STARTDT)
			'''
	outfile = "query_results/for_completion_monthly.csv"
	main(query, outfile)
	query = '''SELECT YEARWEEK(SESSION_STARTDT) AS WEEK, USERID, SESSIONID, VIDEO_DURATION, USR_ACT_TOT_WATCHING_DUR FROM events_data GROUP BY YEARWEEK(SESSION_STARTDT)
			'''
	outfile = "query_results/for_completion_week.csv"
	main(query, outfile)