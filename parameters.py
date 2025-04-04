# types of function: 

# built in function
# user defined 
#     def  
#     lambda 
# callback function 
#higher order function  (HOF)
# first class function (research)  



# arguments -->they are the real/actual values passed to the function 
#  --> they are passed in the paranthesis while function calling
# parameters--> are the variable used to store the values passed as arguments



# def sum(a,b):   
#     print(a,b)
#     return a+b
# sum(2,3)
# sum(-3,20)
# sum("hi","hello")
#positional arguments 


#keyword arguments 

# def mul(b,c,a):
#     print(a,b,c, a*b)
# mul(7,c=5,b=3)


# parameters ---> positional,default , *args,**kwargs



# default -parameters 


# def diff(a,b=0):     ###default parameter
#     print(a,b, a-b)
# diff(10)
# diff(5,3)

# first name 
# last name 
# middle name


# def full_name(f_n,m_n="",l_n=""):
#     print(f_n)
#     print(m_n)
#     print(l_n)
#     print(f_n+m_n , l_n)
# full_name("mani vardhan" , " J")



# def add(a,b=0,*args,c): #
#     print(a,b,c)
#     sum=0
#     for i in range(len(args)):
#         sum+= args[i]
#     return sum
# print(add(1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,c=16))



#keyword arguments:

# def details(**hello):
#      for i in hello:
#           print(i, hello[i])
# details(name="mani",age=20,city="hyd",mob=9848022338,role="dev") 


#positional 
#default    --> parameter=default
#arbituory  --> *parameter_name
#keyword    --> **parameter_name




# def add(a,b=0,*c,**d):
#     print(a,b,c,d)
# add(1,2)


#1.Ascii 
#2.isupper 
#3.
# name="Ram"
# U_C=0
# for i in name:
#     a_v=ord(i)
#     if a_v>=65 and a_v<=90:
#         U_C+=1
#         print(i)
# print(U_C)

# name="Rahul Gandhi"
# u_c=0
# for i in name:
#      if i.isupper():
#           u_c+=1
#           print(i)
# print(u_c)




# string="Once In a Blue MOON"
# uc=0 
# for i in string:
#     if i==i.upper() and i!=" ": #O==O n==N c==C e==E  I==I  B==B  M==M O==O O==O N==N
#         uc+=1
#         print(i)
# print(uc)

# u="ABCDEFGHIJKLMNOPQRSTUVWXYZ"



string="virat kohli is an indian cricket player"
#ascii 
valid=True
for i in string:
    if not i.isalpha() and not i.isspace():
        valid=False 
        break 
if valid:
    print("valid string")
else:
    print("invalid string")
