# Numpy

## Create
```
import numpy as np

np.zeros(10)
np.ones(10)
np.full(10, 3.7)

a = np.array([1, 2, 3, 4, 5])
a[2] = 4

np.arange(10)
np.arange(3, 10)

np.linspace(0, 1, 11)

np.zeros((5, 2))
n = np.array([
    [1, 2, 3],
    [4, 5, 6]
])
n[0, 1] = 20
n[1] = [1, 1, 1]
n[:, 1]
n[:]

np.random.seed(10)
np.random.rand(5, 2)
np.random.randn(5, 2)
np.random.randint(low=0, high=100, size=(5, 2))
```

## Summary

```
a.min()
a.max()
a.sum()
a.mean()
a.std()
```

## Operate

```
a = np.arange(5)
a + 1
(10 + (a * 2)) ** 2
a >= 2
a[a >= 2]

u = np.array([2, 4, 5, 6])
v = np.array([1, 0, 0, 2])
u + v
u * v
u.dot(v)

U = np.array([
    [2, 4, 5, 8],
    [1, 2, 1, 3],
    [5, 2, 8, 9]
])
U.dot(v)

V = np.array([
    [1, 0],
    [2, 1],
    [5, 4],
    [9, 7]
])
U.dot(V)

np.eye(10)

V1 = np.array([
    [1, 2, 1],
    [1, 3, 2],
    [3, 2, 1]
])
V1_inv = np.linalg.inv(V1)
V1.dot(V1_inv)
```

## Transform

```
u = np.array([2, 4, 5, 6])
np.log(n)
np.log1p(n)
np.exp(n)
np.expm1(n)

np.column_stack(u, u)

np.concatenate([u1, u2])
```

