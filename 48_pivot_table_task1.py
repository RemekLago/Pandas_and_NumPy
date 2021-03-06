
import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
sns.set()
tips = sns.load_dataset('tips')
# %%
pv = tips.pivot_table(values='tip', index='sex', columns='day', aggfunc='mean')
pv1 = tips.pivot_table(values=['total_bill', 'tip'],
                       index='sex', columns='day', aggfunc='mean')

pv2 = tips.pivot_table(values='tip', index='sex', columns=['smoker', 'day'])

# %%
tips.pivot_table(values='tip', index='sex', columns='day', aggfunc='mean').\
    plot(kind='bar', cmap='viridis', alpha=0.5)

tips.pivot_table(values='total_bill', index='sex', columns='day',
                 aggfunc='mean').plot(kind='bar', cmap='viridis', alpha=0.5)

tips.pivot_table(values='total_bill', index='day', columns='size',
                 aggfunc='mean').plot(kind='bar', cmap='viridis', alpha=0.5)

tips.pivot_table(values='total_bill', index='time', columns='day',
                 aggfunc='mean').plot(kind='bar', cmap='viridis', alpha=0.5)


vals = tips[['total_bill', 'tip', 'size']]
vals.corr()
