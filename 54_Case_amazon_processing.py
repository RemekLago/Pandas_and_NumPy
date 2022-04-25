
import numpy as np
import pandas as pd
# import data
df = pd.read_csv('data/Consumer_Reviews_Amazon.csv', index_col=0)
# 
df.describe()
# 
for col in df.columns:
    print(col)

df.columns = [col.replace('.', '_') for col in df.columns]
# 
df = df[['name', 'primaryCategories', 'reviews_rating', 'reviews_text']]
df.columns = ['name', 'category', 'rating', 'text']

df.info()
df.describe()
# 
df.to_csv('./data/reviews_clean_amazon.csv')