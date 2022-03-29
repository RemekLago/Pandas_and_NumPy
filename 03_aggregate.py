import pandas as pd
import numpy as np

# generate some data
np.random.seed(0)
s = pd.Series(np.random.randn(20))

minimum = s.aggregate(min)
maximum = s.aggregate(max)
sum_items = s.aggregate(sum)

mean = s.aggregate(np.mean)
std = s.aggregate(np.std)

# 
stats = s.aggregate(['min', 'max', 'sum', 'mean'])
stats_np = s.aggregate([np.mean, np.std, np.median])
