
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
# import seaborn as sns
df = pd.DataFrame(np.random.randn(100, 4),
                  columns=list('ABCD'))

s = pd.Series(np.random.randint(0, 2, 100), name='Flag')
df = df.cumsum()
df.iloc[-1]
bar_data = df.iloc[-1].apply(abs)
bar_data.plot(kind='bar', title="Random generated data", color='green', alpha=0.5)
# multiple bar plot vertical
df1 = pd.DataFrame(np.random.randn(10, 4),
                  columns=list('ABCD'))
df1.plot(kind='bar', cmap='viridis', title='Multiple bar plot', alpha=0.7)
# multiple bar plot horizontal
df2 = pd.DataFrame(np.random.randn(10, 4),
                   columns=list('ABCD'))
df2.plot(kind='barh', cmap='viridis', title='Multiple bar plot', alpha=0.7)

# stacked bar plot vertical
df3 = pd.DataFrame(np.random.randn(10, 4),
                   columns=list('ABCD'))
df3.plot(kind='bar', cmap='viridis', title='Multiple bar plot', alpha=0.7, stacked=True)

# stacked bar plot horizontal
df4 = pd.DataFrame(np.random.randn(10, 4),
                   columns=list('ABCD'))
df4.plot(kind='barh', cmap='viridis',
         title='Multiple bar plot', alpha=0.7, stacked=True)
