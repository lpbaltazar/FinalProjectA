import warnings
warnings.filterwarnings('ignore')

import sys
sys.path.append('../')

import os
import time
import pandas as pd
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
	

	query = '''SELECT DATE(SESSION_STARTDT) AS DATE, COUNT(DISTINCT USERID) AS NUMCUST, COUNT(SESSIONID) AS NUMSESSIONS
				FROM events_data
				WHERE ((USR_ACT_TOT_WATCHING_DUR*1.0)/(VIDEO_DURATION*1.0)) >= 0.80
				GROUP BY DATE(SESSION_STARTDT)
				'''
	outfile = 'query_results/date_count_80.csv'
	main(cursor, query, outfile)

	query = '''SELECT DATE(SESSION_STARTDT) AS DATE, COUNT(DISTINCT USERID) AS NUMCUST, COUNT(SESSIONID) AS NUMSESSIONS
				FROM events_data
				WHERE ((USR_ACT_TOT_WATCHING_DUR*1.0)/(VIDEO_DURATION*1.0)) < 0.80
				GROUP BY DATE(SESSION_STARTDT)
				'''
	outfile = 'query_results/date_count_80_less.csv'
	main(cursor, query, outfile)

	query = '''SELECT DATE(SESSION_STARTDT) AS DATE, COUNT(DISTINCT USERID) AS NUMCUST, COUNT(SESSIONID) AS NUMSESSIONS
				FROM events_data
				WHERE ((USR_ACT_TOT_WATCHING_DUR*1.0)/(VIDEO_DURATION*1.0)) >= 0.60
				GROUP BY DATE(SESSION_STARTDT)
				'''
	outfile = 'query_results/date_count_60.csv'
	main(cursor, query, outfile)

	query = '''SELECT DATE(SESSION_STARTDT) AS DATE, COUNT(DISTINCT USERID) AS NUMCUST, COUNT(SESSIONID) AS NUMSESSIONS
				FROM events_data
				WHERE ((USR_ACT_TOT_WATCHING_DUR*1.0)/(VIDEO_DURATION*1.0)) < 0.60
				GROUP BY DATE(SESSION_STARTDT)
				'''
	outfile = 'query_results/date_count_60_less.csv'
	main(cursor, query, outfile)

	query = '''SELECT DATE(SESSION_STARTDT) AS DATE, COUNT(DISTINCT USERID) AS NUMCUST, COUNT(SESSIONID) AS NUMSESSIONS
				FROM events_data
				WHERE ((USR_ACT_TOT_WATCHING_DUR*1.0)/(VIDEO_DURATION*1.0)) >= 0.50
				GROUP BY DATE(SESSION_STARTDT)
				'''
	outfile = 'query_results/date_count_50.csv'
	main(cursor, query, outfile)

	query = '''SELECT DATE(SESSION_STARTDT) AS DATE, COUNT(DISTINCT USERID) AS NUMCUST, COUNT(SESSIONID) AS NUMSESSIONS
				FROM events_data
				WHERE ((USR_ACT_TOT_WATCHING_DUR*1.0)/(VIDEO_DURATION*1.0)) < 0.50
				GROUP BY DATE(SESSION_STARTDT)
				'''
	outfile = 'query_results/date_count_50_less.csv'
	main(cursor, query, outfile)
