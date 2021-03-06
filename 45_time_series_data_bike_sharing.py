
import seaborn as sns
import zipfile
import os
import wget
import pandas as pd
# !pip3 install wget
sns.set()
#
url = ('https://archive.ics.uci.edu/ml/machine-learning-databases/00275/Bike-Sharing-Dataset.zip')
wget.download(url)
#  preprocessing
z = zipfile.ZipFile('Bike-Sharing-Dataset.zip')
for file in z.namelist():
    if file.endswith('/'):
        os.makedirs(file)
    print(file)

z.extractall('./data/')
# %%
day = pd.read_csv('./data/day.csv', index_col='dteday')
hour = pd.read_csv('./data/hour.csv', index_col='dteday')

# %%
hour.groupby('weekday').size().plot(kind='bar')
hour.groupby('hr').size().plot(kind='bar')

# %%
day.groupby('season').size()
day.groupby('weekday').sum()['registered'].plot(kind='bar')
day.groupby('weekday').sum()['cnt'].plot(kind='bar')
day['temp'].hist()
