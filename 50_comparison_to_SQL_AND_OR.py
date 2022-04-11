
import numpy as np
import pandas as pd

url = ('https://archive.ics.uci.edu/ml/machine-learning-databases/00352/'
       'Online%20Retail.xlsx')

retail = pd.read_excel(url)
# AND
"""
SELECT * FROM retial
WHERE CustomerID='17850' and UnitPrice > 5;
"""

query = retail[(retail['CustomerID'] == '17850') & (retail['UnitPrice'] > 5)]
query2 = retail.query('CustomerID == "17850" and UnitPrice > 5')

# OR
"""
SELECT * FROM retial
WHERE CustomerID='17850' or Country='France';
"""

query = retail[(retail['CustomerID'] == '17850')
               | (retail['Country'] == 'France')]
query2 = retail.query('CustomerID == "17850" or Country == "France"')
