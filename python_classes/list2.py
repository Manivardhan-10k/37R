# append 
# copy 
# extend([])
# count 
# index 
# insert (index,ele(obj))

# clear
# len


# num_list.pop()
# num_list.pop(8)
# print(num_list)


# num_list.remove(1)
# print(num_list)
# num_list=[1,2,3,4,5,6,7,8,9,10] 
# num_list.reverse()
# print(num_list)


# num=[2,3,4,1,6,7,8,5,10,9]
# num.sort(reverse=False)
# print(num)


# num=["hox","how","are","you?","zero"] ##ascii values --american standard code for information interchange 0-127

# num.sort()
# print(num)
# print(min(num))
# print(max(num))


# num=[x**2 for x in range(1,6) if x%2==0]
# print(num)



##problems on lists 


# num=[11,22,66,99,17,121]  #6
# return the num(s) which is not divisible by 11

# 1.iterate the list 
# 2. check whether the num is divisible by 11 

# for ind in range(0,len(num),1):
#     if num[ind] % 11 !=0:     #11 22 66 99 17
#         print(num[ind])



# take a list of num 
# return true only if the first and last elements are even numbers
#else return false 



# count and copy  method implementation


#count
#returns the occurance of the element in the list

# num=[1,2,3,4,5,6,6,7,1,5,3,5]
# ele=5 

# count=0
# for i in range(0,len(num)):
#     if num[i]==ele: #1 2 3 4 5 6 6 7 1 5 3 5
#         count=count+1   #1 2 3
# print(count)

#write a function that replciates the count functionality



# my_list=[1,2,"hello",[1,2],True]
# res=[]

# for i in range(0,len(my_list)):
#     res.append(my_list[i]) ##1 2 "hello"  ,[1,2] True
# print(res)



# take a num list 
# copy the prime numbers into a new list
# num=[1,7,10,22,26,31]
# prime_list=[7,31] 



# num=[1,2,2,3,4,4,5]
# unq_list=[] 

# for ind in range(0,len(num)):
#     if num.count(num[ind])==1: #1  2  1  2 1
#         unq_list.append(num[ind])
# print(unq_list)


# num=[1,2,3,4,5,6]
# new_list=[x for x in num if x%2!=0]
# print(new_list)




