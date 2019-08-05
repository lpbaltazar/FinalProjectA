import warnings
warnings.filterwarnings("ignore")

import sys
sys.path.append('../')

import os
import time
import pandas as pd
import numpy as np

from utils import readChunk
from matplotlib import pyplot as plt
import seaborn as sns

import matplotlib.style as style

sns.set()
style.use('seaborn-poster')

df = readChunk("../sql/query_results/customer_sessioncount_all.csv")

df.FREQUENCY = df.FREQUENCY.astype(int)
plot = df.plot(kind = hist, colormap = 'Pastel2')
plot.set_xlabel('SESSION FREQUENCY')
plot.set_ylabel('NUMBER OF CUSTOMERS')
plt.tight_layout()
plt.savefig('figures/customer_sessioncount_all.png')
