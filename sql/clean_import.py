import warnings
warnings.filterwarnings("ignore")

import sys
sys.path.append("../")

import pandas as pd
import numpy as np
import os
import time

from utils import readChunk, toCSV

cols = ['USERID', 'PRIMARY_FINGERPRINT', 'USER_BROWSER', 'USER_BROWSER_VERSION', 'USER_OS', 'USER_OS_VERSION', 'USER_HOSTADDRESS', 'SESSIONID', 'ORIGINAL_VIDEO_CONTENT_ID', 'VIDEO_CONTENT_ID', 'VIDEO_CONTENT_TITLE', 'ORIGINAL_VIDEO_CATEGORY_ID', 'VIDEO_CATEGORY_ID', 'VIDEO_CATEGORY_TITLE', 'VIDEO_TYPE', 'VIDEO_DURATION', 'SESSION_STARTDT', 'SESSION_ENDDT', 'CLICK_COUNT', 'ADPLAY_COUNT', 'PLAY_COUNT', 'PAUSE_COUNT', 'RESUME_COUNT', 'AB_FLAG', 'SEEK_COUNT', 'BUFFER_COUNT', 'TOTAL_BUFFER_TIME', 'MAX_BUFFER_TIME', 'USR_TOT_WATCHING_DUR', 'USR_ACT_TOT_WATCHING_DUR', 'ISP_PROVIDER', 'ISMOBILE', 'MOBILE_DEVICE', 'ISP_TAG', 'MOBILETYPE', 'APP_TAG', 'THREE_G_TAG', 'CONTENT_TYPE', 'IPCOUNTRY', 'SUBDIVISION_1', 'SUBDIVISION_2', 'IPCITY', 'APP_VERSION']
remove_comma = ['VIDEO_CONTENT_TITLE', 'VIDEO_CATEGORY_TITLE', 'ISP_TAG']

def cleanData(data_dir):
	for f in sorted(os.listdir(data_dir)):
		if f.endswith(".csv"):
			file = os.path.join(data_dir, f)
			df = readChunk(file)
			df = df[cols]
			for col in remove_comma:
				df[col] = df[col].astype(str)
				df[col] = df[col].apply(lambda x: x.replace(",", " ") if x.replace(",", " ") else x)
			toCSV(df, file, index = False)

if __name__ == '__main__':
	cleanData("../../events/sql/december")
    cleanData("../../events/sql/january")
    cleanData("../../events/sql/february")
    cleanData("../../events/sql/march")
    cleanData("../../events/sql/april")
    cleanData("../../events/sql/may")