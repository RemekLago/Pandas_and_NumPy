
import pandas as pd
import numpy as np

df = pd.DataFrame(np.random.randn(20, 5),
                  columns=list('abcde'),
                  index=list('abcdefghijklmnoprstu'))
col_a = df.a

mask = df.a > 0
out = df[mask]

# or
out = df.[df.a > 0]
mask2 = (df.a > 0) & (df.c > 0)
out2 = df[mask2]

# or 
out2 = (df.a > 0) & (df.c > 0)
mask3 = (df.a > 0) | (df.c > 0)
out3 = df[mask3]
