import pandas as pd
import numpy as np

# loading the data
ten_pl = pd.read_csv('data/ten.csv', index_col=0)
plw_pl = pd.read_csv('data/plw.csv', index_col=0)

ten = ten_pl.copy()
plw = plw_pl.copy()
# preprocessing data
ten.columns = ['Open', 'High', 'Low', 'Close', 'Volume']
plw.columns = ['Open', 'High', 'Low', 'Close', 'Volume']
# merge on index, inner
out = pd.merge(ten, plw, how='inner', left_index=True, right_index=True)

# merge with suffixes
out = pd.merge(ten, plw, how='inner', left_index=True,
               right_index=True, suffixes=('_TEN', '_PLW'))

#  merge on index, outer
out1 = pd.merge(ten, plw, how='outer', left_index=True, right_index=True)

# # merge with suffixes
out1 = pd.merge(ten, plw, how='outer', left_index=True,
                right_index=True, suffixes=('_TEN', '_PLW'))

# bonus
ten['Change'] = ten['Close'] / ten['Close'].shift(1) - 1
plw['Change'] = plw['Close'] / plw['Close'].shift(1) - 1

ten['Flag'] = ten['Change'] > 0
plw['Flag'] = plw['Change'] > 0

ten['Flag'] = ten['Flag'].apply(int)
plw['Flag'] = plw['Flag'].apply(int)

correlation_matrix = out.corr()
