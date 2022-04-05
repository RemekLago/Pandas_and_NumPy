
import pandas as pd
import numpy as np
df1 = pd.DataFrame(np.random.rand(10, 4), columns=list('abcd'))
df2 = pd.DataFrame(np.random.rand(10, 4), columns=list('abcd'))
df3 = pd.DataFrame(np.random.rand(10, 4), columns=list('abcd'))

df3 = df1.append(df2)
df3.reset_index()
del df3[0]
df4 = df1.append(df2).reset_index().drop('index', axis=1)
df5 = df1.append(df2, ignore_index=True)
