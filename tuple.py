# tuple
# list -[]
# dict -{key:value}
# set -{1,2,3,,"hi"}
# tuple-()

# we can multiple values in tuple 
##it is immutable
# it is an ordered collection

# my_tuple=(1,2,3,"hello",True,1,2,3,4) 

# last_ind=len(my_tuple)-1
# print(my_tuple[len(my_tuple)-1])

# my_tuple[9]="new"
# print(my_tuple)

# for i in range(0,len(my_tuple),1):
# for i in range(len(my_tuple)):
#     print(my_tuple[i])



# my_tuple=(1,2,3,"hello",True,1,2,3,4,False,1,1,1,1,1) 
# print(my_tuple.count(0))
# print(my_tuple.index(1))




#Problem solving 


# my_tuple=(8,6,5,4,9,1,9,8,3,4,5,8)
# num=int( input("enter the number u want to find: ")  )##2nd occurence
# count=0
# occ= int(input("enter the occurance u want to find: "))
# # print(my_tuple.index(8))
# if my_tuple.count(num)>=occ:
#     for i in range(len(my_tuple)): ##0 1 2 3 4 5 6 7
#         if my_tuple[i]==num:
#                          count+=1 #1 2 3
#         if count==occ:
#           print(i)
#           break  #to terminate the break after the requirement is done
# else:
#    print( "the num is present less than ",occ," times")




##req: find the even  numbers in the even indexes
# my_tup=(1,2,3,4,5,1,2,4,8,3,6,8)
# ##2  8  6
# for i in range(len(my_tup)):
#     if i%2==0  and my_tup[i]%2==0:
#         print(my_tup[i])



# details={
#     "name":"manivardhan",
#     "age":19,
#     "citizen":"indian"
# }
##check the person is eligible to vote or not 
## if eligible add a new key "eligble":True

# if details["age"]>18:
#     details["eligible"]=True
# else:
#     details["eligible"]=False
#     print("wait for some time")
# print(details)



# voters=[{"name":"manivardhan",
#     "age":19,
#     "citizen":"indian"},{    "name":"vikas",
#     "age":20,
#     "citizen":"indian"}]


# ##task 1
# for i in range(len(voters)): ##0
#     print(voters[i]["age"])



# name="madam"  ## madam
# rev=""
# # print(len(name))
# for i in range(len(name)-1,-1,-1):
#     rev+=name[i]    
# if rev==name:
#     print("palindrome")
# else:
#     print("not palindrome") 



# s=2 
# e=5 
#14

#task 2
##unq-the element must be present only once
##add it to the list if unq
tup=(1,2,5,8,3,9,7,2,5,7,12,65,8)
unq=[1,3,9,12,65]
# unq_tup=set(tup)
# unq_tup=tuple(unq_tup)
# print(unq_tup)
# tup=tuple(set(tup))
# print(tup)