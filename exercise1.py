import numpy as np

a = np.array([1, 3, 5, 7])
print(a)
# array([1, 3, 5, 7])

b = np.arange(4)
# array([0, 1, 2, 3])
print(b)

c = np.arange(2, 10, 1)
# array([2, 3, 4, 5, 6, 7, 8, 9])
print(c)

d = np.linspace(0, 10, 6)
print(d)
# array([ 0.,  2.,  4.,  6.,  8., 10.])

e = np.array([[1,2,3],[4,5,6]])
print(e)
# array([[1, 2, 3], [4, 5, 6]])

f = np.zeros((2,3))
print(f)
# array([[0., 0., 0.],[0., 0., 0.]])

g = np.ones((2,3))
print(g)
# array([[1., 1., 1.], [1., 1., 1.]])

print(a+b)
print(c**2)

print(e.shape)

print(e.T)

print("_" * 60)
x = np.random.random((3, 5))
print(x)

print(x.sum())
print(x.min())
print(x.max())
print(x.mean())