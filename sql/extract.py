import warnings
warnings.filterwarnings("ignore")

import sys
sys.path.append("../")

import re
import os
import time
import numpy as np
import pandas as pd

from utils import readChunk, toCSV

def removeLurkers(df):
	df["lurkers"] = df[["USERID", "PRIMARY_FINGERPRINT"]].apply(lambda x: 1 if re.search(x[1], x[0]) else 0, axis = 1)
	df = df.loc[df.lurkers == 0]
	print(len(df))
	return(df)

def extractColumns(data_dir, outdir):
	print(data_dir)
	for f in sorted(os.listdir(data_dir)):
		if f.endswith('.csv'):
			file = os.path.join(data_dir, f)
			df = readChunk(file)
			df.dropna(subset=['USERID'], inplace = True)
			df.USERID = df.USERID.astype(str)
			df.PRIMARY_FINGERPRINT = df.PRIMARY_FINGERPRINT.astype(str)
			df = removeLurkers(df)
			outfile = os.path.join(outdir, f[-12:])

			toCSV(df, outfile, index = False)
			
if __name__ == '__main__':
	extractColumns("../../events/2018/12", "../../events/sql/december")
	extractColumns("../../events/2019/01", "../../events/sql/january")
	extractColumns("../../events/2019/02", "../../events/sql/february")
	extractColumns("../../events/2019/03", "../../events/sql/march")
	extractColumns("../../events/2019/04", "../../events/sql/april")
	extractColumns("../../events/2019/05", "../../events/sql/may")
