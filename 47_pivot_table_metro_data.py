
import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
sns.set()
url = ('https://archive.ics.uci.edu/ml/machine-learning-databases/00492/'
       'Metro_Interstate_Traffic_Volume.csv.gz')

# loading dataset
metro = pd.read_csv(url, compression='gzip', parse_dates=True, index_col='date_time', parse_dates=True)
metro = metro.loc['2021-01-01':]

# plotting traffic
traffic = metro.iloc[:, -1]
traffic.plot()
tr = traffic.resample('M').sum()
tr.plot()
# pivot tables
metro.pivot_table(data=metro, values='traffic_volume',
                  index='weather_main').plot(kind='bar')
