
import pandas as pd
import numpy as np

idx = pd.Index(['8732', '3823', '4892', '8542'])
df = pd.DataFrame(np.random.randn(4, 5),
                  index = idx,
                  columns=list('abcde'))