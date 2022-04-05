import pandas as pd
import numpy as np

df = pd.DataFrame(np.random.randn(10, 4),
                  columns=['one', 'two', 'three', 'four'])

for row in df.values:
    switch = np.random.choice([0, 1])
    if switch:
        i = np.random.choice([0, 1, 2, 3])
        row[i] = np.nan
        
        
df = df.fillna(0)
df['one'] = df['one'].fillna(0)
df.fillna(df.mean())
df.fillna(df.median())
df['four'] = df['four'].fillna(df['four'].mean)
