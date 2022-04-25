
import pandas as pd
import numpy as np
import seaborn as sns
sns.set()
# import data
df = pd.read_csv('data/reviews_clean_amazon.csv', index_col=0)
# plotting categories
df['category'].value_counts()
df['category'].value_counts().plot(kind='pie')
#  plotting ratings frequency
df['rating'].value_counts().sort_index().plot(kind='bar', legend=True, title='Frequency')
#  extract top 3 most rating products
a = df.groupby('name').count()['rating'].rename('count').nlargest(3).plot(kind='bar')
# extract top 3 high rating products
b1 = df.groupby('name').mean()['rating'].rename('mean_rating').nlargest(3)
b2 = df.groupby('name').agg('mean').rename(columns={'rating':'mean_rating'}).nlargest(3, columns='mean_rating')
b3 = df.groupby('name').agg('mean')
# extract bottom 3 products
b1 = df.groupby('name').mean()['rating'].rename('mean_rating').nsmallest(3)
b2 = df.groupby('name').agg('mean').rename(columns={'rating':'mean_rating'}).nsmallest(3, columns='mean_rating')