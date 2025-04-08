# l2=l[2:5:]
# print(l2)

#comprehension:
# num_list=[2,3,4,5,6,7,8,9]
# even=[]
# for i in range(len(num_list)):
#     if  num_list[i]%2==0:
#         even.append(num_list[i])
# print(even)

# even2=(num_list[ind] for ind in range(len(num_list)) if num_list[ind]%2==0)
# print(list(even2))

##[expression     iteration     condition]
#it returns a generator object
#we can convert the object using type conversion 


# num_list=[[1,2,3],[4,5,6],[7,8,9]]
# max_val=[]
# for  i in range(len(num_list)): #0 1 2
#     maximum=num_list[i][0]  #1 4 7
#     for j in range(len(num_list[i])):   #0 1 2
#         if num_list[i][j]>maximum :   #1>1 2>1  5>4 6>5  7>7 8>7 9>8
#             maximum=num_list[i][j]
#     max_val.append(maximum)
# print(max_val)

# num_list=[[1,2,3],[4,5,6],[7,8,9]]
# max_list=[]
# for i in num_list:
#      for j in i:
#           if j== max(i):
#            max_list.append(j)
# print(max_list) 

# num_list=[[1,2,3],[4,5,6],[7,8,9]]
# max_lst=[ j for i in num_list  for j in i if j==max(i)] ##3==3   6==6 9==9
# print(max_lst)


# lst=[1,2,3,4,5,5,5,5,5,5]
# five=[ele**2 for ele in lst  if ele==5]
# print(five)




# details={"p1":"Shiva","p2":"Mahesh","p3":"Rakesh"}
# new={}
# for person in details:
#     if details[person].lower().startswith("m"):##shiva  mahesh rakesh
#         new[person]=details[person]  ##{"p2":mahesh}
# print(new)

# n2={details[key]:key   for key in details   if details[key][0].lower()=="m"}
# print(n2)


##problem solving 
# LCM -- Least Common Multiple
#2 numbers 
# n1=100  #10 20 30 40 50 60...
# n1=15   ##6 12 18 24 30 36 42 48 54 60 66 72......
# n2=50  ##20 40 60 80 100.......
# big=max(n1,n2)
# small=min(n1,n2)
# if big%small==0:
#     print(f"{big} is the LCM")
# else:
#     temp=big #20 40 60
#     while True:
#      if temp%small==0 and temp%big==0: #20%6==0  20%20==0     40%6  40%20   60%6 60%20
#         print(f"{temp } is the LCM")
#         break
#      temp+=big

import math
# print(math.lcm(15,50))




# 15  15 30 45 60 75 90 105 120 135 150 165..
# 50 50 100 150 200..



# HCF --Highest Common Factor 
# GCD -- Greatest common Divisor

# n1= 17   ### 1 2 5 10
# n2= 20    ### 1 2 4 5 10 20
# big=max(n1,n2)
# small=min(n1,n2)
# hcf=0
# if big%small==0:
#     print(f"{small} is the HCF/GCD")
# else:
#     for i in range(1,small+1): #10
#      if small%i==0 and big%i==0:
#         hcf=i 
#         break
#     print(f"{hcf } is the HCF/GCD")
# print(math.gcd)