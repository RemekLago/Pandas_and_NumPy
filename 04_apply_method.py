import math
import pandas as pd
import numpy as np

# generate some data
np.random.seed(0)

# sigma = 10, mean = 5
s = pd.Series(10 * np.random.randn(20) + 5)

# apply method
s.apply(abs)
s.apply(float.is_integer)
s.apply(int)

s.apply(lambda x: 100 * x)
s.apply(lambda y: abs(y))

s_norm = s.apply(lambda x: (x - np.mean(s) / np.std(s)))

sigmoid = s_norm.apply(lambda x: 1 / (1 + np.exp(x)))

def more_complex(x):
    import math
    return math.sqrt(np.exp(x))
    
s.apply(more_complex)