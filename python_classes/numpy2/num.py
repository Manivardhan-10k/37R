# numpy 
# numerical python

#it is fast 
# it is built in c 
# continginity --  entire array is stored in single block
# vectorization  
# mutlti threading-  thread process  

# array ()
# zeros()
# ones()
# arange()
# linspace()- > (s-e)  equal parts

import numpy as np 


# print(np.sum([[1,2,3],[4,5,0]],axis=0))


# arr=[
#     [1,2,3],
#     [4,5],
#     [7,8,9,10]
# ]
# max_row=0
# for i in range(len(arr)): #0 1 2
#     if len(arr[i])>max_row:  #3>0  2>3   4>3
#         max_row=len(arr[i])  #3 4
# for i in arr: ## [1,2,3]  [4,5]  [7 8 9 10]
#     while len(i)<max_row:    # 3<4 4<4    2<4  4<4
#         i.append(0)  #  1230   4 5 0 0
# print(np.sum(arr,axis=1))


#square matrix 

#mean 
# print(np.mean([[1,2,3],[4,5,6],[7,8,9]],axis=1))
#sum of ele/no of ele


#median

# print(np.median([1,2,3,4,5,6])) 

# arr=[1,2,3,4,5,6]
# mid= len(arr)//2  #3
# if len(arr)%2==0:
#     add=arr[mid]+arr[mid-1]  #4+3 
#     print(add/2)   
# else:
#     print(arr[mid])



#reshape 
# print(np.reshape([1,2,3,4,5,6],(6,1)))  #1,4   6

# print(np.reshape(np.arange(12), (2, 2, 3)))


# a=[
#     [
#         [ 0 , 1 , 2],
#   [ 3,  4 , 5]
#   ],

#  [
#  [ 6 , 7 , 8],
#   [ 9 ,10 ,11]
#   ]
 
#  ]


# print(np.reshape(np.arange(24),(2,2,6))) #4 ,2 3


# print(np.reshape(np.arange(100),(10,5,2)).flatten())

# a = np.array([1, 2])
# b = np.array([3, 4])
# print( np.concatenate((a,b)))

# p = np.array([[1], [2]])  ##  1,2     1,1
# q = np.array([[3], [4]])
# np.concatenate((p, q), axis=1)



# a = np.array([[10, 10, 30], [50,990,90]])
# # print(np.where(a > 15))
# # print(np.where(a == 99))
# print(np.where(a % 10 == 0))

#unique
# print(np.unique([[1,2,3,2],[1,3,1,2],[3,4,5,6]])) 


# mean    -->avg
# median  -- > middle number
# reshape 
# concate 
# flatten   --> array.flatten()
# where 
# unique 
# num=5
# arr=[
#     [1,2,3],
#     [4,3,5]
#     ]
# [1,2]