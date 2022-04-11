
import numpy as np
import pandas as pd
url = ('https://archive.ics.uci.edu/ml/machine-learning-databases/00352/'
       'Online%20Retail.xlsx')

retail = pd.read_excel(url)
# %% top n rows
"""
SELECT * FROM retail
ORDER BY Quantity DESC
LIMIT 5;
"""
query = retail.nlargest(5, columns='Quantity')

# %% bottom n rows
"""
SELECT * FROM retail
ORDER BY Quantity
LIMIT 10;
"""
query = retail.nsmallest(5, columns='Quantity')
