
import pandas as pd
import numpy as np
df = pd.read_csv('./data/aapl_us_d.csv', index_col=0)
df.iloc[:10]
df.iloc[2:10]
df.iloc[3:]
df.iloc[[1]]
df.iloc[[1, 4]]
df.iloc[:: 2]

df.iloc[:, :2]
df.iloc[1:6, 1:2]
