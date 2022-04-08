import pandas as pd
import numpy as np
# splitting by hash
s = pd.Series(['#sport#good#time', '#workout#free#time', '#summer#holiday#hot'],
              name='hashtag')
s = s.str.split('#')
hash_1 = s.str.get(1)
hash_2 = s.str.get(2)
hash_3 = s.str.get(3)

# concatenating by row
df_concat_by_row = pd.concat([hash_1, hash_2, hash_3], ignore_index=True)
string = df_concat_by_row.str.cat(sep=' ')
# concatenating by column
df_concat_by_col = pd.concat([hash_1, hash_2, hash_3], axis=1)

# other split
split_2 = s.str.split('#', expand=True)
split_2 = split_2.drop(0, axis=1)
# replace
s.str.replace('#', '_')
