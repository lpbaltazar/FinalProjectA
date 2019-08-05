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
	# query = '''SELECT YEARWEEK(SESSION_STARTDT, 1) AS WEEK, USERID, COUNT(SESSIONID)
	# 			FROM events_data
	# 			GROUP BY YEARWEEK(SESSION_STARTDT, 1), USERID
	# 			HAVING (SUM(USR_ACT_TOT_WATCHING_DUR)/SUM(VIDEO_DURATION))*100 >= 70
	# 			'''
	# outfile = 'query_results/customer_sessioncount_week.csv'
	# main(cursor, query, outfile)

	query = '''SELECT EXTRACT(YEAR_MONTH FROM SESSION_STARTDT) AS MONTH, USERID, COUNT(SESSIONID) AS FREQUENCY
				FROM events_data
				GROUP BY EXTRACT(YEAR_MONTH FROM SESSION_STARTDT), USERID
				HAVING ((SUM(USR_ACT_TOT_WATCHING_DUR)*1.0)/(SUM(VIDEO_DURATION)*1.0)) >= 0.70
				'''
	outfile = 'query_results/customer_sessioncount_month.csv'
	main(cursor, query, outfile)

	query = '''SELECT USERID, COUNT(SESSIONID) AS FREQUENCY
				FROM events_data
				GROUP BY USERID
				HAVING ((SUM(USR_ACT_TOT_WATCHING_DUR)*1.0)/(SUM(VIDEO_DURATION)*1.0)) >= 0.70
				'''
	outfile = 'query_results/customer_sessioncount_all.csv'
	main(cursor, query, outfile)


	query = '''SELECT DATE(SESSION_STARTDT) AS DATE, USERID, COUNT(SESSIONID) AS FREQUENCY
				FROM events_data
				GROUP BY DATE(SESSION_STARTDT), USERID
				HAVING ((SUM(USR_ACT_TOT_WATCHING_DUR)*1.0)/(SUM(VIDEO_DURATION)*1.0)) >= 0.70
				'''
	outfile = 'query_results/customer_sessioncount_day.csv'
	main(cursor, query, outfile)
