import numpy as np


np.arange(10)

np.arange(1,10)

np.arange(1,10,2)

np.arange(1,10,0.5)

np.arange(1,10,dtype='float64')


np.arange(1,10,dtype='int32')

arr = np.arange(0,10)

arr.ndim

arr.shape

arr.size

arr.dtype

arr.itemsize


arr2 = np.arange(1,10,dtype='int64')
arr2.itemsize


arr.itemsize * arr.size


arr2.itemsize * arr2.size

np.asarray([1,2,3,4,5])

list1=[[1,2,3,4,5],[6,7,8,9,10]]

arr3 = np.asarray(list1)


listzeros = np.zeros((3,4),dtype='int32')


np.linspace(1,4,num=4)
np.linspace(1,4,num=8)
np.linspace(1,4,num=8,endpoint=False)


np.random.random((3,4))

rarr = np.random.random((3,4))

np.max(rarr,axis=0)
np.max(rarr,axis=1)


np.min(rarr,axis=0)
np.min(rarr,axis=1)

np.median(rarr,axis=0)
np.median(rarr,axis=1)

new_rarr=np.reshape(rarr,(12,))

new_rarr1=np.reshape(rarr,(12,1))

rarr[:,:]

rarr[1:3,:]

rarr[1:2,:]

rarr[:,1:]

rarr[:,1:3]


rarr[:,0:3]


rarr[1:3,1:3]



rarr[[0,2],:]

rarr[[1,2],[0,3]]

rarr[[0,1],[2,3]]


rarr[:-1,:]

rarr[-1:,:]

rarr[:,-1:]

rarr[:,:-1]

rarr[-2:,:]

rarr[:-2,:]

rarr[-1:,-1:]


rarr[:-1,:-1]























