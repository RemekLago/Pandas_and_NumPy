
import numpy as np
import pandas as pd
url = ('https://archive.ics.uci.edu/ml/machine-learning-databases/00352/'
       'Online%20Retail.xlsx')

retail = pd.read_excel(url)
# %% group by
"""
SELECT CustomerID, count(*)
FROM retial
GROUP BY CustomerID;
"""
cust_id = retail.groupby('CustomerID').size()
countries = retail.groupby('Country').size()
countries.plot(kind='bar')

# %% compute new cols
retail['Revenue'] = retail['Quantity'] * retail['UnitPrice']

# %% group by
"""
SELECT CustomerID, avg(Revenue), count(*)
FROM retial
GROUP BY CustomerID;
"""
revenue_by_cust_id = retail.groupby('CustomerID').aggregate({'Revenue': np.mean, 'CustomerID': np.size}).\
    rename(columns={'Revenue': 'AverageRevenue',
           'CustomerID': 'Count CustomerID'})


# %% making InvoiceDateday column
retail['InvoiceDateDay'] = retail['InvoiceDate'].dt.day
query = retail.groupby('InvoiceDay').agg({'Revenue': sum})
query.plot(kind='bar', color='black', alpha=0.5, title='sales by day')
# grouping by InvoiceDateDay
mask = (retail['InvoiceDate'] >
        '2010-12-09') & (retail['InvoiceDate'] < '2010-12-10')
day_9 = retail[mask]
day_9['Hour'] = day_9['InvoiceDate'].dt.hour

query = day_9.groupby('Hour').agg({'Revenue': np.sum})
query.plot(kind='bar', alpha=0.5)
