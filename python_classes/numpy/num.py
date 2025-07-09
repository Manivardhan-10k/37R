##numpy 
##numerical python 
##third party module

import numpy as np
print(np)


#stack     heap 


# homogenous          heterogenous

# single type        different types



#array 
# print(np.array([1,"hello",3]))
# print(type(np.array([1,2,3])))
# print(np.array((1,2,3,4,1,2))) 

#zeros(shape,datatype)
# print(np.zeros(3))
# print(np.zeros(5))
# print(np.zeros(3,int))
# print(np.zeros((2, 2),int))
# print(np.zeros((4, 5),int))
# np.zeros((3, 1))



#ones 
# array=np.ones((5,5))
# print(array[0][4])


np_ar=(np.arange(1,100,2))
# out=[]
# for i in range(1,100,2):
#     out.append(i)
# print(out)

# print(len(np_ar))
# np_ar[0]=100
# print(np_ar)

# print(type(out))


# array 
# zeros 
# ones 
# arange
#linspace()
#sum() axis


# print(np.linspace(1,100,3))#1 20 40 60 80 100   




#sum 
# print(np.sum([1,2,3,4]))

# print(sum([1,2],[4,6]))

# print(np.sum([[1,2],[4,6]])) #2 X 2
# print(np.sum([[1,2,3,],[4,5,6]]))
# axis=0   sum of elements in the same elements 
#axis =1  sum of elements in the same row

##vectorization
#vector



# res=[]
# arr=[[1,2,3],[4,5,6]]   ##axis=1  [6 ,15]
# for i in range(len(arr)): ##0 1
#     s=0
#     for j in range(len(arr[i])): #0 1 2
#         s+=arr[i][j]   ##[0][0]  [0][1]  [0][2]
#                        # #[1][0]  [1][1] [1][2]
#     res.append(s)
# print(res)
        
    
    
