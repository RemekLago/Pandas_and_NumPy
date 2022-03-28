from pickletools import stackslice
import pandas as pd
import numpy as np

# Example 1
s = pd.Series(4)

# Example 2
s_def = pd.Series(data=[21, 34, 54], index=['Adam', 'Tomek', 'Pawel'], name='age')


# Example 3
A = np.random.random(10)
s = pd.Series(A)

# Example 4
stocks = {'Apple': "USA", 'CD Project': "Poland", "Amazon": "USA"}
series = pd.Series(stocks, name="country")

# Example 5
stocks_price = {'Apple': 916, 'CD Project': 137, "Amazon": 54}
stocks_price_series = pd.Series(stocks_price, name='stock prise')

stocks_price_array = stocks_price_series.values

apple_price = stocks_price_series['Apple']

'Apple' in stocks_price_series

# Example 6
np.random.seed(0)
B = np.random.random(20)
s = pd.Series(B)
s[0]
s[1]
s[5:10]