import pandas as pd
import numpy as np

df = pd.DataFrame(np.random.randn(10, 5),
                  columns=list('abcde'))
df.query('(a < b)')

df.query('(a < b) & (b < c)')

df.query('(a < b) | (b < c)')

df2 = df.round(1)
df.query('c == 0.2')
df.query('c == [0.2, 0.5]')

df.query('c != 0.2')
df.query('[0.2] in c')
