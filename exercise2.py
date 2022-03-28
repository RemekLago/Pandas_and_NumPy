import numpy as np

a = np.array(42)
b = np.array([1, 2, 3, 4, 5])
c = np.array([[1, 2, 3], [4, 5, 6]])
d = np.array([[[1, 2, 3], [4, 5, 6]],
              [[1, 2, 3], [4, 5, 6]]])

print(a.ndim)
print(b.ndim)
print(c.ndim)
print(d.ndim)

arr1 = np.array([1, 2, 3, 4], ndmin=5)

print(arr1)
print('number of dimensions :', arr1.ndim)

print("-" * 50)
arr2 = np.array([1, 2, 3, 4])
print(arr2[0])
print(arr2[2] + arr2[3])

print("-" * 50)
arr3 = np.array([[1,2,3,4,5], [6,7,8,9,10]])
print('2nd element on 1st row: ', arr3[0, 1])

print("-" * 50)
arr3 = np.array([1.1, 2.1, 3.1])
newarr = arr3.astype('i')

print(newarr)
print(newarr.dtype)

print("-" * 50)
arr4 = np.array([1, 2, 3, 4, 5])
x = arr4.copy()
arr4[0] = 42

print(arr4)
print(x)
print("-" * 50)
arr5 = np.array([1, 2, 3, 4, 5])
x = arr5.copy()
y = arr5.view()

print(x.base)
print(y.base)
print("-" * 50)

arr = np.array([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12])
newarr = arr.reshape(4, 3)
print(arr)
print(newarr)
print("-" * 50)

arr = np.array([[[1, 2], [3, 4]], [[5, 6], [7, 8]]])

for x in np.nditer(arr):
  print(x)
print("-" * 50)

arr7 = np.array([[1, 2], [3, 4]])
arr8 = np.array([[5, 6], [7, 8]])
arr = np.concatenate((arr7, arr8), axis=1)
print(arr)

print("-" * 50)





