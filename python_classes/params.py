# num =1234657875 
# di=7 
# pos=7 ,9 


# functions
#built in functions: len print range max min  

# user defined function:
# def identifier( user_number  ) : ##  function name
    # logic  user_number
    #return value 
# identifier( 9848022338) 
#arguments  --> should always be a real value
#parameters --> they are the values passed as arguments 

#lambda function:

# sum_function= lambda      : p

# sum_function= lambda x,y: x+y
# print(sum_function(n1,n2))



# print("hello")
# def sum_numbers():
#     n1=int(input("enter the number"))
#     n2=int(input("enter the number"))
#     return n1+n2
# print(sum_numbers())


# mul=lambda x=int(input("number1: ")),y=int(input("number 2: ")) :x*y
# print(mul())


#higher order function    -->a fucntion which takes/accepts another function as a parameter
#callback  -- function calling another function  


# sum=lambda x,y :x+y 

# def is_odd():
#     n=sum(5,7)  ##12
#     return n%2!=0  # 12%2!=0


# print(is_odd())



# def mul(n1,n2,func):
#     return func(n1*n2 )  ##add_1(n1*n2)

# def add_1(m):
#     print(m)
#     return m+1 


# print(mul(2,3,add_1))





# def login():
#     user_name=input("enter username: ")
#     password=input("enter password: ")
#     if user_name=="manivardhan" and password=="secret":
#         return True 
#     else:
#         return False

# def show_data():
#     if login():  
#          return ("welcome user, this is your data!")
#     else:
#         return ("pls login!!")
# # print(show_data())


# def show_prod():
#     if login():
#         return {"item":"samsung mobile"}
#     else:
#         return "pls login first!!"
# print(show_prod())






#
n1=int(input("enter number 1: "))#50
n2=int(input("enter number 2: "))#10 

np1=0
np2=0
maximum=max(n1,n2) #50
prime_count=0
prime_num=2
mul=1
while  prime_count<=maximum:  # 0<=50
    fact=0
    for i in range(2,prime_num):
        if prime_num%i==0:
            fact+=1
            break
    if fact==0:
        prime_count+=1
        if prime_count==n1 :
            np1=prime_num
            print(prime_num)
        if prime_count==n2:
            np2=prime_num
            # mul=mul*prime_num
    prime_num+=1
# print(mul-1)
print(np1,np2)





    









