import pandas as pd
import numpy as np

# generatint some data
np.random.seed(0)

A = np.random.randint(0, 10, 10)
series = pd.Series(A)

# attributes
series.dtype
series.iloc[3] 
series.index
series.name
series.shape
series.plot

array_A = series.values

N = np.random.randn(10)
M = np.random.randn(10)

series_N = pd.Series(N)
series_M = pd.Series(M)

# basic methods
series_N.abs()
series_N.add(series_M)
series_N.subtract(series_M)
series_N.divide(series_M)
series_N.drop_duplicates()
series_N.dropna()
series_N.idxmax()
series_N.idxmin()
series_N.count()
series_N.cumsum()
series_N.cummin()
series_N.cummax()
series_N.value_counts()
series_N.sum()
series_N.std()
series_N.describe()

# histogram
hist_data = pd.Series(np.random.randn(10000))
hist_data.hist(bins=80, color='red')

# top n, 3 
top_3 = series_N.nlargest(3)

# bottom n, 3 
bottom_3 = series_N.nsmallest(3)

# quantiles
q_1 = series_N.quantile(0.25)
q_2 = series_N.quantile(0.5)
series_N.round(3)

# method shift
shift_1 = series.shift(1)
shift_2_replace_0 = series.shift(2).fillna(0)

# sort
sorted_series = series.sort_values()
sorted_series = series.sort_values(ascending=False)