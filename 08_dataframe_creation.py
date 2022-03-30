

import pandas as pd
import numpy as np
df = pd.DataFrame(data=[12, 34, 23])

df2 = pd.DataFrame(data=[[12, 54, 32],
                         [53, 23, 74]], index=['first', 'second'],
                   columns=['col1', 'col2', 'col3'])

df3 = pd.DataFrame(data=[[12, 54, 32],
                         [53, 23, 74],
                         [23, 54, 74]], index=['first', 'second', 'third'],
                   columns=['col1', 'col2', 'col3'])
d = {'one': pd.Series([1, 2, 3]),
     'two': pd.Series([4, 5, 6])}

df4 = pd.DataFrame(d)
d1 = {'one': pd.Series([1, 2, 3]),
      'two': pd.Series([4, 5, 6]),
      'flag': ('yes', 'no', 'yes')}

df5 = pd.DataFrame(d1)

#
d2 = {'one': pd.Series([1, 2, 3, 4, 5]),
      'two': pd.Series([4, 5, 6])}

df6 = pd.DataFrame(d2)

#
d3 = {'one': pd.Series(np.random.randn(100)),
      'two': pd.Series(np.random.randn(100)),
      'three': pd.Series(np.random.randn(100))}
df6 = pd.DataFrame(d3)

df.index
df.columns

list_of_dict = [{'apple': 1, 'orange': 4},
                {'apple': 3, 'orange': 3, 'mango': 2}]
df7 = pd.DataFrame(list_of_dict)

for col in df.columns:
    print(col)
big_letters = [col.upper() for col in df7.columns]
df7.columns = big_letters
