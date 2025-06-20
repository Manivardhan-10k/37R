# lst=[1,2,3,4,5,6,7,8,9,10]   #[2,4,6,8,10,1,3,5,7,9] 

# lst=[1,2,3,2,1,4,5]  # [1,2,3,4,5,"*","*"]
# temp=[]  #1,2,3,4,5
# for i in lst:
#     if i not in temp:
#         temp.append(i)
# count=len(lst)-len(temp)
# # print(count)
# for i in range(count):  #0 1   X2
#     temp.append("*")
# print(temp)



# lst=[1,2,3,1,2,4,5,2,1]  ##[1,2,3,"*","*,"4,5,"*","*"]
# temp=[]
# for i in lst:
#     if i not in temp:  #1 2 3 1
#         temp.append(i)
#     else:
#         temp.append("*")
# print(temp)

# lst=[1,2,3,1,2,4,2,2,5,5,2,3,1]
# temp=[] 
# for i in lst:
#     if i not in temp:
#         temp.append(i)
# for i in temp: #1  2
#     # print( f" { i} is present {lst.count(i)} times")
#     count=0
#     for j in lst: # 1 2 3 1 2 4 2 2 5 5 2 3 1
#         if i==j:
#             count+=1 #5
#     print(i, " is present ", count, " times")


#anagram 
# lst1=[1,2,3,3]
# lst2=[3,1,3,2]

# lst1.sort()
# lst2.sort() 
# print(lst1==lst2)
# is_same=True
# if len(lst1)!=len(lst2):
#     print("not anagram lists")
# else:
#     for i in lst2:  #3
#         if lst1.count(i)!=lst2.count(i): # 2 2
#             is_same=False
#             print("not anagram")
#             break
# if is_same==True:
#     print("both are anagrams")

# def is_prime(n):
#     if n>=2:
#         fact=0
#         for i in range(2,n):
#             if n%i==0:
#                 fact+=1
#                 break
#         if fact==0:
#             return True
#         else:
#             return False
#     else:
#         return False

# num=35   # 1  5 7  35
# factors=[]
# prime_factors=[] #5 7
# for i in range(1,num+1,1): #1   ...... 35
#     if num%i==0: # 5 7
#         factors.append(i)
#         if is_prime(i): # True True
#             prime_factors.append(i)
# print(factors,"\n",prime_factors)


# details={
#     "name":"teja",
#     "marks":[90,95,99,83,45,35]
#     #"total"=total
# }
# total=0 
# for key in details:  ##name marks
#     if key=="marks":
#         for i in details[key]: #marks
#             total=total+i #447
# details["total"]=total
# print(details)


# CRUD
# create
# Read 
# Update
# Delete



# employees={
#     "vinay":45000,
#     "ramesh":60000,
#     "rakesh":200000
# }
# # 305000/3 =101666
# total=0
# for key in employees:
#     total+=employees[key]
# employees["average"]=total/len(employees)
# print(employees)




#find the missing number 
#[1,3,5,6,7]   #2,4


#calculate the avg marks in subject 


# sqrt(49) # 7  floor 7   ceil 7
# sqrt(26)#5.054564 floor 5  ceil 6

num=2026
perfect=True 
square=0
for i in range(1,num): #    1  6      25
    if i*i==num: #5*5  6*6
        square=i
        break
    if i*i>num :  #36>26
        perfect=False
        break
if perfect==True:
    print(square)
else:
    print("not perfect")
        

