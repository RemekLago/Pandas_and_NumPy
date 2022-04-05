
import pandas as pd
import numpy as np

df = pd.read_csv('data/aapl_us_d.csv', sep=',', index_col=0, skiprows=10)
df1 = pd.read_csv('data/aapl_us_d.csv', sep=',', index_col=0, nrows=100)

# read tsv
df2 = pd.read_csv('data/aapl_us_d.tsv', sep='\t', index_col=0)

# read xls
df3 = pd.read_excel('data/aapl_us_d.xls', na_values='?', index_col=0)
df4 = pd.read_excel('data/aapl_us_d.xls', index_col=0, sheet_name='microsoft')

# read html
df3 = pd.read_html('data/aapl_us_d.html', header=0, index_col=0)[0]

# read www
df4 = pd.read_html('https://www.biznesradar.pl/gielda/indeks:WIG20')[0]
