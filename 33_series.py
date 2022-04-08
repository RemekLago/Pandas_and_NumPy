
import pandas as pd
import numpy as np
s = pd.Series(['apple', '    Microsoft', np.nan,
              '  Google  ', 'Amazon'], name='Stock')
s.str.strip()
s.str.upper()
df = pd.DataFrame(np.random.randn(10, 2),
                  columns=['     ID number  ', '   Price  '])
df.columns = df.columns.str.strip()
df.columns = df.columns.str.replace(' ', '_')
