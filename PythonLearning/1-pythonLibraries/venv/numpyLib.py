import numpy as np

a = np.array([1,2,4], int)
b = np.array([[1.3,4.5,4.],[3.2,5.6,6.]], dtype="float16")
print(b)

# Get Dimension
print(a.ndim)
print(b.ndim)

# Get Shape
print(a.shape)
print(b.shape)

# Get Type
print(a.dtype)

# Get Size (amount of bytes)
print(a.itemsize)
print(b.itemsize)

# Get total size
print(b.size)

# Get elements:
c = np.array([[1,2,3,4,5,6,7],[8,9,10,11,12,13,14]])
print(c)

print(c[1,5])
print(c[1,:])
print(c[0,:])
print(c[:,3])
print(c[0, 1:-1:2])