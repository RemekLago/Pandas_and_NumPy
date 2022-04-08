
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
sns.set()


ts = pd.Series(np.random.randn(1000),
               index=pd.date_range('2019-01-01', periods=1000))
ts1 = ts.cumsum()
ts1.plot()
ts2 = ts1.cummin()
ts2.plot()
ts3 = ts1.cummax()
ts3.plot()

df = pd.DataFrame(np.random.randn(1000, 5),
                  index=pd.date_range('2019-01-01', periods=1000),
                  columns=list('ABCDE'))
df1 = df.cumsum()
df1 = df.plot(kind='line')
df1 = df.plot(kind='bar')

df1 = df.plot(kind='kde')

df1 = df.plot(kind='hist')

df1 = df.plot(kind='box')

df1 = df.plot(kind='box')

df1 = df.plot(kind='destiny')

df['B'].plot()
df.iloc[5].plot(kind='bar')
