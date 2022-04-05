import pandas as pd
import numpy as np
d1 = {'date': ['2019-01-01', '2019-01-01', '2019-01-02', '2019-01-02'],
      'id': ['0001', '0002', '0003', '0004'],
      'product_id': ['0343', '0523', '0151', '0022']}
d2 = {'date': ['2019-01-01', '2019-01-02', '2019-01-02', '2019-01-03'],
      'id': ['0001', '0002', '0003', '0004'],
      'price': ['99', '149', '59', '199']}

df_left = pd.DataFrame(d1)
df_right = pd.DataFrame(d2)

# inner
df_inner = pd.merge(df_left, df_right, how='inner', on=['date', 'id'])

# outer
df_outer = pd.merge(df_left, df_right, how='outer', on=['date', 'id'])

#  left join
df_left = pd.merge(df_left, df_right, how='left', on=['date', 'id'])

#  right join
df_right = pd.merge(df_left, df_right, how='right', on=['date', 'id'])
