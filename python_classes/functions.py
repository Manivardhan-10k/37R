# function :
# it is a reusable block of code
# function id defined with def keyword



# num=5 
# num=num**2
# print(num) 

# num=7 
# num=num**2
# print(num)



# def  power():   ##function identifier
#     print("hi")

# power()  ## function calling /function invoking 
# power()
# power()
# power()
# power() 

# it should print the square of the number

#parameters

#arguments
#they should always be a real value
# n=10
# def square(no): ##parameters
#     print(no)
#     print(no**2)
# square(n)  ##arguments are passed while function calling
# square(5)
# square(7)



#return 


# def addition(p_1,p_2):
#    return  p_1+p_2
# addition(10,8) 
# total=addition(5,7)
# print(total)  


#predefined function
##user-defined 


#lambda function 
#it is a function assigned to variable
#lambda follwed by : return value

# sub= lambda : "hello from lambda"
# print(sub())




# mul=lambda p1,p2  :  p1*p2
# total=mul(7,9)
# print(total,mul(6,8,9))


# num1=(input("enter the first number: "))
# num2=input("enter the second number: ")

# def division(n1,n2):
#     return int(n1)/int(n2 )
# print(division(num1,num2))

# def sum(n1,n2):
#     return  n1+n2
# def is_even(n):
#     return n%2==0
# total_sum=sum(10,3)
# print(is_even(total_sum))



# def factor(n): #1 2 3 6
#     out=[]
#     for i in range(1,n+1,1):
#         if n%i==0:
#             out.append(i)
#     # print(out)
#     return out
# print(factor(6))


# var=lambda x=input("enter the number"), y=input("Enter number ") : x+y 
# print(var())