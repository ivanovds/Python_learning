import numpy as np

a = np.array([1,2,4], int)
b = np.array([[1.3,4.5,4.],[3.2,5.6,6.]], dtype="float16")
print(a.ndim)
print(b)
print(' Get Dimension')
print(b.ndim)
print('Get Shape')
print(a.shape)
print(b.shape)
print('Get Type')
print(a.dtype)
print('Get Size (amount of bytes)')
print(a.itemsize)
print(b.itemsize)
print('Get total size')
print(b.size)
print('Get elements:')
c = np.array([[1,2,3,4,5,6,7],[8,9,10,11,12,13,14]])
print(c)
print(c[1,5])
print(c[1,:])
print(c[0,:])
print(c[:,3])
print(c[0, 1:-1:2])
print('3d array:')
d = np.array([[[1,2],[3,4]],[[5,6],[7,8]]])
print(d)
print(d[0,:,0])
print('replace')
d[:,0,:] = [[0,0],[0,0]]
print(d)

print('Different types of Arrays:')
print('All 0s matrix')
print(np.zeros((2,3,3)))
print('All ones')
print(np.ones((3,3)))
print('Any other values:')
print(np.full((4,2), 55))
print('Any other values(full_like):')
print(np.full_like(b, 44))
print(' or:')
print(np.full(b.shape, 33, b.dtype))

print('Random decimal(десятичная дробь) numbers:')
print(np.random.rand(3,4))
print(np.random.random_sample(b.shape))
print('Random integer numbers:')
print(np.random.randint(5,100, size = (3,4)))
print(np.random.randint(10, size = (10,5)))

print('The identity matrix (единичная)')
print(np.identity(5))

print('repeat an array')
arr = np.array([[1,2,3]])
r1 = np.repeat(arr, 3, axis=0)
print(r1)

output = np.ones((5,5))
z = np.zeros((3,3))
z[1,1] = 9
output[1:4,1:4] = z
print(z)
print(output)

print('Copying of arrays')
a = np.array([1,2,3])
b = a #Not just a copy!!!
b[0] = 50
print(a)
c = a.copy() # Just a copy
c[2] = 300
print(c)
print(a)


print('Find the determinant:')
d = np.identity(4)
print(np.linalg.det(d))

print('Statistics')
stats = np.array([[1,-20,3],[-4,5,2]])
print(stats)
print(np.min(stats, axis = 1)) # минимальное в первом множестве и во втором
print(np.min(stats, axis = 0)) # пересечение\
print(np.sum(stats, axis=0)) #суммирует поэлементно

print('Reorganizing arrays:')
before = np.array([[1,2,3,4,5],[6,7,8,9,10]])
print(before)
after = before.reshape((5,2))
print(after)

print('Vertically stacking vectors:')
v1 = np.array([1,2,3,4])
v2 = np.array([5,6,7,8])
v3 = np.vstack((v1,v2,v1,v2))
print(v3)
h1 = np.hstack((v1,v2))
print(h1)

print('Load data from file')
filedata = np.genfromtxt('data.txt', delimiter=',')
filedata = filedata.astype('int32')
print(filedata)

print('Advanced indexing')
print(filedata > 5) # true or false
print(filedata[filedata > 5])
print(np.any(filedata > 20, axis=0))
print(np.all(filedata > 20, axis=0))
print(np.any((filedata > 20) & (filedata < 30), axis=0))
print(np.any((filedata > 20) & (filedata < 30))) #just one true ore one false

print(' ~ means NOT')
print(((filedata > 20) & (filedata < 30)))
print(~((filedata > 20) & (filedata < 30)))
