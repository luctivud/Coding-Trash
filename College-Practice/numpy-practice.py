''' Notes of Udit Gupta // 25 May 2020 '''

import numpy as np

'''Checking the version of numpy'''
# print(np.__version__)


'''Type of nd array'''
# arr = np.array(100)
# print(type(arr))


'''Checking the dimension of arrays'''
# li = [x for x in range(5)]
# arr = np.array(li)
# print(arr.ndim)

# arr = np.array([[1, 1, 1], [2, 2, 2]])
# print(arr.ndim)

# arr = np.array([[[1, 1, 1], [2, 2, 2]], [[1, 1, 1], [2, 2, 2]]])
# print(arr.ndim)
# print(arr.size)
# print(arr.itemsize)


''' Create ndarrays with zeros'''
# arr = np.zeros(10) #length
# arr = np.zeros(10, dtype=int) #datatype
# arr = np.zeros((2, 3), dtype=int) #pass the dimension of array as tuple and optional datatype
# print(arr)


''' Create ndarrays with ones'''
# arr = np.ones(5, dtype=str)
# arr = np.ones((2, 3), dtype=int)
# print(arr)


'''
WHY NUMPY WHEN WE HAVE LIST :
>>> Less Memory
>>> Fast
>>> Easy to understand
'''
import sys
# li =[1, 2, 3, 4, 5, 6, 7, 8, 9]
# print(sys.getsizeof(1)*len(li))
# arr = np.array(li)
# print(arr.size*arr.itemsize)

import time
# l1 = range(0, 1000000)
# l2 = range(1000000, 2000000)
# A1 = np.array(l1)
# A2 = np.array(l2)

# start = time.time()
# result1 = [x+y for x,y in zip(l1, l2)]
# print((time.time() - start)*1000)

# # For numpy both size shoulf be same
# start = time.time()
# result2 = A1 + A2
# print((time.time() - start)*1000)


'''Shape of arrays'''
# arr = np.array(range(1, 100))
# print(arr.shape)

# arr = np.array([[1, 2, 3], [1, 2, 3]], dtype=np.int8) #float16
# print(arr.shape)
# print(arr.itemsize)


''' Numpy to generate random numbers '''
# rand generates random float from 0 to 1 of given size
# x = np.random.rand(10)
# print(x)

# x = np.random.rand(2, 3)
# print(x)

# randint returns a random integer from given range start, end-1
# x = np.random.randint(1, 11, 10) #start, end, size
# print(x)


''' Choice '''
# Suppose we want to assign any number of questions from a given set of questions[] only
# li = range(1, 5)
# x = np.random.choice(li, size=10)
# print(x)
# x = np.random.choice(li, size=(10, 5))
# print(x)
