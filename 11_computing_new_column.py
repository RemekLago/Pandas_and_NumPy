
import pandas as pd
import numpy as np
df = pd.read_csv('./data/aapl_us_d.csv', index_col=0)
df.columns = ['Open', 'High', 'Low', 'Close', 'Volume']
df['Average'] = (df['Open'] + df['Close']) / 2.
df["Daily"] = df['Close'] / df['Close'].shift(1) - 1
df = df.assign(avg=(df['Open'] + df['Close']) / 2.)

max_daily_change = df['Daily'].aggregate(max)
min_daily_change = df['Daily'].aggregate(min)
avg_daily_change = df['Daily'].aggregate(np.mean)
df['Daily'].hist(bins=100)
df['Flag'] = df['Daily'] > 0
df['Flag'].aggregate(sum)
days_with_positive_return = df['Flag'].aggregate(sum) / df['Flag'].aggregate('count')
