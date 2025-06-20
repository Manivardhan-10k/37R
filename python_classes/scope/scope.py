# SCOPE:
# count=0
# if  True:
#     count=100
# print(count)


# def hello():
#     c=100 
#     "this is a string"
#     "this is a string"
#     "this is a string"
#     "this is a string"
#     "this is a string"
#     "this is a string"
#     "this is a string"
#     "this is a string"
#     "this is a string"
#     "this is a string"
#     print(c,"from the block")
# hello()
# print(c)

# 1.Local :
# the variable can be accessed within the block


# def outer():
#     count=100
#     def inner():
#        nonlocal count  
#        print(count,"from the inner function")
#        count+=50
#     inner()
#     print(count)
# outer()
# 2:Enclosed Scope

# count=0
# def hello():
#     count=100 
#     print(count,"local")
# hello() 
# print(count,"from global") 
 
#global

# name="empty"
# def use_name():
#     global name 
#     name=input("enter the name: ")
# use_name()
# print(name) 
#global 

# L -local
# E -enclosed
# G -global

# nonlocal :
# to access the variables in the outer scope/block

# global:
# to make the variable global/to be accessed outside the scope
# B- builtin 



# def acc():
#     global bal
#     bal=0
#     def add_money():
       
#         # bal+=1000
#         print(bal,"from the add function")
#     def reduce_money():

#         # bal-=500
#         print(bal,"from the reduce function")
#     add_money()
#     reduce_money()
#     # return bal 
# print(acc())
# print(bal,"from outer")


# count=0 
# def inc():
#     global count
#     count+=100
# inc()
# inc()
# inc()
# inc()
# inc()
# inc()
# print(count)

# global_var="hello"
# def name():
#     # global global_var
#     print(global_var)
#     # global_var="hello world"
# name()
# print(global_var)


# count=1000
# def outer():
#     count=100
#     def inner():
#         count=10
#         print(count)
#     inner()
# outer()




# user="manivardhan" 
#user="vikas"
#user="raju"
# def change1():
#     global user
#     user="raju"
# def change2():
#     global user
#     user="vikas"
# change2()
# change1()
# print(user)


# ##Find the second largest in the list
# l=[49,45,47]
# #sec=32
# # l=list(set(l))
# # l.sort( reverse=True)
# # print(l[1])
# max=l[0]  ##1
# sec_max=l[1] ##2 
# for i in range(len(l)): #0   1   2   1
#     if l[i]>max and l[i]>sec_max: #
#         sec_max=max #1  3 32 45
#         max=l[i] #3   45  47
#     if l[i]<max and l[i]>sec_max:
#         sec_max=l[i] #32
# print(max,sec_max)

