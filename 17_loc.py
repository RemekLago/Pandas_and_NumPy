
import pandas as pd
import numpy as np

df = pd.DataFrame(np.random.randn(20,5),
                  columns=list('abcde'),
                  index=list('abcdefghijklmnoprstu'))
col_a = df.loc[:,'a']
col_b = df.loc[:,'b']
col_a_b = df.loc[:, ['a','b']]
col_b_c_d = df.loc[:, 'b':'d']
row_a = df.loc['a', :]
row_a2 = df.loc[['a'], :]
row_a_c =df.loc[['a', 'c'], :]
row_a_col_a = df.loc['a', 'a']
row_a_d_col_b_d = df.loc['a':'d', 'b':'d']
