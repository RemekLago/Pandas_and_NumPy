
import numpy as np
import pandas as pd
url = ('https://archive.ics.uci.edu/ml/machine-learning-databases/00352/'
       'Online%20Retail.xlsx')

retail = pd.read_excel(url)
# %% explorating dataset
retail.info()
desc = retail.describe()

cols = [col for col in retail.columns]

retail.head()
retail.tail()
# %% preprocessing
# drop rows with null
retail = retail[retail['CustomerID'].notnull()]
# convert type to string
retail['CustomerID'] = retail['CustomerID'].apply(lambda x: str(int(x)))
# exclude Quantity less than zero
retail = retail[retail['Quantity'] >= 0]
# %%
"""
SELECT * FROM retial;
"""
query = retail
# %%
"""
SELECT Quantity, UnitPrice, CustomerID FROM retial;
"""
query = retail[['Quantity', 'UnitPrice', 'CustomerID']]
# %%
"""
SELECT Quantity, UnitPrice, CustomerID FROM retial;
LIMIT 10;
"""
query = retail[['Quantity', 'UnitPrice', 'CustomerID']][:10]
query2 = retail[['Quantity', 'UnitPrice', 'CustomerID']].head(10)

# %%
"""
SELECT * FROM retial
WHERE CustomerID='17850';
"""

query = retail[retail['CustomerID'] == '17850']
query2 = retail.query('CustomerID == "17850"')
