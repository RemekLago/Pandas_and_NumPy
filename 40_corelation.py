
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
# importing data
df = pd.read_csv('data/ten.csv', index_col=0)
df.columns = ['Open', 'High', 'Low', 'Close', 'Volume']
clean_price = df[['Open', 'High', 'Low', 'Close']]
# computing correlation matrix
corr_matrix = clean_price.corr()
#  corr between Series
df['Open'].corr(df['Close'])
# plot correlations matrix using matplotlib
plt.matshow(corr_matrix)
# plot correlations matrix using seaborn
sns.heatmap(corr_matrix)
