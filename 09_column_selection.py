
import pandas as pd
import numpy as np
df = pd.read_csv('./data/aapl_us_d.csv', index_col=0)
df.columns = ['Open', 'High', 'Low', 'Close', 'Volume']
open_price = df['Open']
open_price2 = df.iloc[:, 0]
high_price = df['High']
close_price = df.Close
volume = df.Volume
last_column = df.iloc[:, -1]
two_columns = df[['Open', 'Close']]
two_columns2 = df.iloc[:, [0, 3]]

few_columns = df.iloc[:, [0, 4]]
few_columns2 = df.iloc[:, :-2]
