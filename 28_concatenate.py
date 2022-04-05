
import pandas as pd
import numpy as np
df1 = pd.DataFrame(np.random.rand(10, 4), columns=list('abcd'))
df2 = pd.DataFrame(np.random.rand(10, 4), columns=list('abcd'))
df3 = pd.DataFrame(np.random.rand(10, 4), columns=list('abcd'))
s = pd.Series(np.random.rand(10), name='x')
# concat
# by rows
df = pd.concat([df1, df2, df3], ignore_index=True)
df_a = pd.concat([df1, df2, df3])
df_a.reset_index()
# different column name
# by columns
df4 = pd.DataFrame(np.random.rand(10, 4), columns=list('abcd'))
df5 = pd.DataFrame(np.random.rand(10, 4), columns=list('efgh'))
df_b = pd.concat([df4, df5], axis=1)

#  outer, inner
df4 = df4[::2]
df6 = pd.concat([df4, df5], axis=1, join="outer")
df7 = pd.concat([df4, df5], axis=1, join="inner")
df6.reset_index()
df7.reset_index()

# append Series to DataFrame
df8 = pd.concat([df3, s], axis=1)
