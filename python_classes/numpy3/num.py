#numpy methods 

#mean 
#median 
#reshape 
#concatenate 
#flatten  array(nested).flatten()
#where where(a>/= < condition)
#unique --> it converts the entire array as a unique array 

import numpy as np
from numpy import linalg as la

# arr= np.array([1,2,3,40,5,61,7,8])
#clip 
# print(arr) 


# print(np.clip(arr,3,10))


# a1=[[1,2,3]]
# a2=[4,5,6]

# the no of rows in first matrix shoould be equal to columns in second matrix 

#dot 
# print(np.dot(a1,a2))

# a1=[
#     [1,2,3],   #7 + 16 +27   =50
    
#     [4,5,6]  #28+40+54 =122
# ]
# a2=[[7],[8],[9]]

# print(np.dot(a1,a2))


# a=np.array([[1,2,3,4]])
# print(np.transpose(a))


# arr=np.array([[1,2],[4,5]])  #2x2
# print(la.inv(arr))

# print(np.random.randn())
# print(np.random.randn(4))
# print(np.random.randn(2, 3))
# print(np.random.randn(1, 2))


# print(np.array([[1,0],[3,4]]).shape) #

# print(np.array([1, 2, 3]).ndim)
# print(np.array([[1, 2], [3, 4]]).ndim)
# print(np.array([[[1], [2]], [[3], [4]]]).ndim) 




# AR -> augmented reality   --> combination   real+fake
# vr-> virtual reality      --> completely fake 



# clip 
# transpose 
# dot 
# linalg.inv 
# randn()
# shape 
# ndim 
# size()


# array=[
#     [4,5,6],
#     [7,8,9]
# ]
# transpose=[]
# for i in range(len(array[0])): #0 1 2
#     row=[]
#     for j in range(len(array)): #0 1
#         row.append(array[j][i])#[47] [58] [6 9]
#     transpose.append(row) #[[47], [5 8] [69]]
# print(transpose)
# print(np.transpose(np.array(array)))



# arr=[
#     [1,2,3],
#     [4,5,6],
#     [7,8,9]
# ]
# num=8   # (2,1)
# for i in range(len(arr)):
#     for j in range(len(arr[i])):
#         if arr[i][j]==num:
#             print(f"{num} is in {i+1} row  and {j+1} column")
# for n in arr:
#     if num in n:
#         print(arr.index(n),n.index(num))

    
