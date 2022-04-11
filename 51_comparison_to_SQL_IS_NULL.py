
import numpy as np
import pandas as pd
url = ('https://archive.ics.uci.edu/ml/machine-learning-databases/00352/'
       'Online%20Retail.xlsx')

retail = pd.read_excel(url)
# %% isnull
"""
SELECT *
FROM retail
WHERE InvoiceNo is null;
"""
retail[retail['InvoiceNo'].isnull()]
retail[retail['StockCode'].isnull()]
# %% is not null
"""
SELECT *
FROM retail
WHERE InvoiceNo is not null;
"""
retail[retail['InvoiceNo'].notnull()]
