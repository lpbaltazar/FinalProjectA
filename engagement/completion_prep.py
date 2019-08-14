import warnings
warnings.filterwarnings("ignore")

import sys
sys.path.append("../")

import os
import time
import pandas as pd
import numpy as np

from utils import readChunk, toCSV
from matplotlib import pyplot as plt
import seaborn as sns

import matplotlib.style as style

sns.set()
style.use('seaborn-poster')
style.use('bmh')

df = readChunk("tv_completion.csv", header = None)
df.VIDEO_DURATION = pd.to_numeric(df.VIDEO_DURATION, errors = 'coerce')
df.rename(columns = {0:'USERID', 1: 'TITLE', 2:'VIDEO_DURATION', 3:'WATCHING_DURATION'}, inplace = True)

df['CONTENT_COMPLETION'] = (df.WATCHING_DURATION/df.VIDEO_DURATION)*100
toCSV(df[['CONTENT_COMPLETION']], 'content_completion.csv', index = False)