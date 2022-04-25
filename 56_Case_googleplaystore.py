
import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib as plt
sns.set()
df = pd.read_csv('data/googleplaystore.csv')

# preprocessing
df.info()
df.columns = [col.replace(' ', '_') for col in df.columns]
col = [col for col in df.columns]

# drop
df = df.drop(10472)
df = df.reset_index()

# column reviwes to numeric
df.Reviews = pd.to_numeric(df.Reviews)

# categories frequency
tmp = df.groupby('Category').size().rename('Count')
tmp.plot(kind='bar', color='purple', alpha=0.5, title='Categories')

#  type frequency
tmp2 = df.groupby('Type').size()
tmp2.plot(kind='pie')

# 
df = df[['Genres', 'Rating', 'Type']]
tmp2 = df.groupby(['Genres', 'Type']).agg({'Rating':['count', 'mean']})
tmp2.columns = ['_'.join(x) for x in tmp2.columns.ravel()]
tmp2 = tmp2.sort_values('Rating_count', ascending=False)
tmp2.plot(kind='bar', subplots=True, cmap='viridis')

#  top 5 rating products
top_5 = tmp2.nlargest(5, columns='Rating_count')
top_5.plot(kind='pie', subplots=True)