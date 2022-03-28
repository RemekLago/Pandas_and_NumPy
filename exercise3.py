from numpy import random

x = random.randint(100)

print(x)
print("-" * 50)


x = random.randint(100, size=(3, 5))

print(x)
print("-" * 50)

x = random.rand(5)

print(x)
print("-" * 50)

x = random.choice([3, 5, 7, 9], p=[0.1, 0.3, 0.6, 0.0], size=(100)) #with probability

print(x)
print("-" * 50)

from numpy import random
import matplotlib.pyplot as plt
import seaborn as sns

#sns.distplot(random.normal(size=1000), hist=False)
#plt.show()
print("-" * 50)
from numpy import random

x = random.binomial(n=10, p=0.5, size=10)

print(x)
print("-" * 50)

from numpy import random
import matplotlib.pyplot as plt
import seaborn as sns

sns.distplot(random.normal(loc=50, scale=5, size=1000), hist=False, label='normal')
sns.distplot(random.binomial(n=100, p=0.5, size=1000), hist=False, label='binomial')

plt.show()
