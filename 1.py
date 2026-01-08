import numpy as np
import random

array = np.array([1,2,3,4,5])
print(type(array))

array2 = np.array([1,2,3,'hello'])
print(array2)

array = array+1

print(array)

array3 = np.zeros(5, dtype=np.uint8)
print(array3)

array4 = np.array([1,2,3,4,5,6],dtype=np.float16)
print(array4)

array5 = np.array([[1,2,3],[4,5,6],[7,8,9]])
print(array5)
print(array5.ndim)
print(array5.shape)
print(array5.size)


array6 = np.arange(1,100,2)
print(array6)

array7 = np.random.permutation(np.arange(1,100,2))
print(array7)

for i in range(100):
    print(np.random.randint(1,10)) #high is not included
    
# print('-------')
# for i in range(100):
#     print(random.randint(0,10))


array8 = np.random.rand(2,3)
print(array8)
array8 *= 10
print(array8)

array9 = np.random.permutation(np.arange(1,10))
print(array9)
array9 = array9.reshape(3,3)
print(array9)

array10 = np.random.permutation(np.arange(1,37))
print(array10)
array10 = array10.reshape(6,6)
print(array10)
array10 = array10.reshape(3,12)
print(array10)
array10 = array10.reshape(2,18)
print(array10)
array10 = array10.reshape(4,9)
print(array10)


array11 = np.random.permutation(np.arange(1,11))
print(array11)
sorted_array = np.sort(array11)
print(sorted_array)

array12 = np.arange(1,10).reshape(3,3)
print(array12)
print(array12[0:3, 0:3])
print(array12[0, 0])
print(array12[1:2, 0:2])


array13 = np.arange(1,50).reshape(7,7)
print(array13)
array13[2:5, 2:5] = 0
print(array13)

array14 = np.arange(1,11)
print(array14)
even = array14[array14%2==0]
print(even)

print(array14%2==0)

print(array14[np.array([True,True,True,False,False,False,True,True,True,False])])

print(array14[[2,4,6]])

print(array14[array14<5])

array15 = np.arange(1,11)
array16 = np.arange(101, 111)
array17 = array15 + array16
print(array17)

# list1 = [1,2,3]
# list2 = [2,3,4]
# list3 = []
# for i, j in zip(list1,list2):
#     list3.append(i+j)
    
# print(list3)

array18 = np.arange(1,10).reshape(3,3)
array19 = np.arange(101,110).reshape(3,3)
array20 = array18+array19
print(array20)

array21 = np.arange(1,5).reshape(2,2)
array22 = np.arange(1,5).reshape(2,2)
array23 = array21.dot(array22)
print(array23)


array24 = np.arange(1,6)
# array24 = array24*2+3
# print(array24)

def change(x):
    return x*2+3

array24 = change(array24)
print(array24)