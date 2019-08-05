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

	# query = '''SELECT YEARWEEK(SESSION_STARTDT, 1) AS WEEK, USERID, (SUM(USR_ACT_TOT_WATCHING_DUR)/SUM(VIDEO_DURATION))*100 AS AVGCOMPLETION
	# 			FROM events_data
	# 			GROUP BY YEARWEEK(SESSION_STARTDT, 1), USERID'''
	# outfile = 'query_results/week_average_completion.csv'
	# main(cursor, query, outfile)

	# query = '''SELECT EXTRACT(YEAR_MONTH FROM SESSION_STARTDT) AS MONTH, USERID, (SUM(USR_ACT_TOT_WATCHING_DUR)/SUM(VIDEO_DURATION))*100 AS AVGCOMPLETION
	# 			FROM events_data
	# 			GROUP BY EXTRACT(YEAR_MONTH FROM SESSION_STARTDT), USERID'''
	# outfile = 'query_results/month_average_completion.csv'
	# main(cursor, query, outfile)

	query = '''SELECT USERID, (SUM(USR_ACT_TOT_WATCHING_DUR)/SUM(VIDEO_DURATION))*100 AS AVGCOMPLETION
				FROM events_data
				GROUP BY USERID
			'''
	outfile = 'query_results/all_average_completion.csv'
	main(cursor, query, outfile)

