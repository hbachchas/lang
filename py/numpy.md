[numpy.c_](https://docs.scipy.org/doc/numpy-1.15.0/reference/generated/numpy.c_.html)  
[numpy.hstack](https://docs.scipy.org/doc/numpy-1.15.0/reference/generated/numpy.hstack.html)
```python
x = np.array([1, 2, 3])
y = np.array([4, 5, 6])
print(np.hstack((x,y)))
print(np.c_[x,y])
print(np.hstack([  np.c_[x,y]  ]))
print('-------------')
x = np.array([[1],[2],[3]])
y = np.array([[2],[3],[4]])
print(np.c_[x,y])
print(np.hstack([x,y]))
```

Random array generation with numpy
```python
# print(help(np.random.standard_normal))
print(np.random.standard_normal((2,3)))
print(np.random.randn(2,3))
```

Shuffled array with module: random
```python
a = range(0,5)
random.sample(a, len(a))
```
