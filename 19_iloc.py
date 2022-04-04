
import pandas as pd
import numpy as np

df = pd.DataFrame(np.random.randn(20, 5),
                  columns=list('abcde'),
                  index=list('abcdefghijklmnoprstu'))

# iloc[row_indexer, column_indexer]
col_1 = df.iloc[: , 0]
col_a_b = df.iloc[: , 0:2]
col_a_b2 = df.iloc[: , [0,1]]
col_last = df.iloc[: , -1]
col_last2 = df.iloc[:, 4]
col_by_2 = df.iloc[:, ::2]
row_1 = df.iloc[0, :]
row_1_ = df.iloc[[0], :]
row_1_ = df.iloc[[0, 5, 6], :]
row_last = df.iloc[-1, :]
row_last_ = df.iloc[[-1], :]
row_by_2 = df.iloc[::2, :]
col_1_last_row_1_last = df.iloc[[0, 19], [0, 4]]
col_1_last_row_1_last = df.iloc[2:8, 1:]
