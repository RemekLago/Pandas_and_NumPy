
import seaborn as sns
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
!pip3 install seaborn
sns.set()
""" statistics
count() - number od non-null observations
sum()
mean()
median()
min()
max()
std()
var() - unbiased variance
skew() - skewness - 3 moment
kurt() - kurtosis - 4 moment
quantile()
apply()
cov()
corr()
"""
# importing data
df = pd.read_csv('data/ten.csv', index_col=0)
df.columns = ['Open', 'High', 'Low', 'Close', 'Volume']
clean_price = df[['Open', 'High', 'Low', 'Close']]
volume = df[['Volume']].copy()

#  Series
cum_vol = volume.cumsum()
#  plot cumulative sum of volume
cum_vol.plot()
# plot moving average
close = df['Close']
close_rol_avg = close.rolling(window=30).mean()
close.plot()
close_rol_avg.plot(style='k--')
# moving averages
close.plot(color='black')
for i in [5, 8, 12, 60, 65, 70]:
    close_rol_ang = close.rolling(window=i).mean()
    close_rol_ang.plot(alpha=0.5)

# simple startegy
close.plot(color='black')
for i in [5]:
    close_roll_min = close.rolling(window=i).min()
    close_roll_min.plot()
    close_roll_max = close.rolling(window=i).min()
    close_roll_max.plot()

# DataFrame
clean_price.rolling(window=20).mean().plot()
close.plot(color='black')

# DataFrame, std
close.rolling(window=15).std().plot()
close.plot(color='black')

# DataFrame subplots
clean_price.rolling(window=20).mean().plot(subplots=True)
# apply, custom indicator
example_ind = close.rolling(window=20).apply(lambda x: (x - x.mean()).mean())
example_ind.plot()
