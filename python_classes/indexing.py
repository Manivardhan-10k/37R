l=[1,2,3,4,5,6,7,8,9,10,11,12,13,14,15]
list2=[]

# for i in range(1,7):
#     list2.append(l[i])
# print(list2)

# #slicing
# list3=l[1:7:1]
# print(list3)


# print(l[::])
# print(l[2::])
# print(l[:5:])
# print(l[1::2])
# print(l[1::2])


l4=[]
for i in range(len(l)-1,-1,-1) :  #  
    l4.append(l[i])
print(l4) 


# l5=l[2:13:]
# print(l5)

# s1="sracecars"   #racecar 
# if s1==s1[::-1]:
#     print("palindrome")
# else:
#     print("not palindrome")


# nested=[[1,2,3],[4,5,6],[7,8,9]]
# final=[]
#a list can contain any type of datatype

# for i in range(0,len(nested),1):#for iterating over the main list(nested)
#     for j in range(0,len(nested[i]),1):#for iterating the sub list(nested[i])
#        final.append( nested[i][j])
# print(final)



# nested=[[1,2,3],[4,5,6],[7,8,9]]
# final=[]
# for i in nested:#[1,2,3]
#     for j in i: #1 2 3    4 5 6    7 8 9
#         final.append(j)
# print(final)
nested=[[-11,-2,-3],[-4,-5,-6],[-1,-1,-9]]    ##[-2,-4,-1]
largest=nested[0][0]
for i in nested:
    for j in i: #1 2 3   4 5 6
        if j>largest: #1>0 1    2>1 3>2 4>3 5>4  1>6  1>6 9>6
            largest=j  #1 2 3 4 5 6  9
print(largest)


