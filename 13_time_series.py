import pandas as pd
import numpy as np

index = pd.date_range('01-01-2020', periods=10_000)
df = pd.DataFrame(np.random.randn(10_000), index=index)
df_cumsum = df.cumsum()
df_cumsum.plot(kind="line")
df_1 = pd.DataFrame(np.random.randn(10, 3), columns=list('ABC'))
df_2 = pd.DataFrame(np.random.randn(10, 3), columns=list('ABC'))
sum_df = df_1 + df_2
sub_df = df_1 - df_2
multi_df = df_1 * df_2
div_df = df_1 / df_2
dex_df = df_1 ** 2
