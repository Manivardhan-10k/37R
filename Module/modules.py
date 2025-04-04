# error handling methods: 

# try:
#     #code to be executed 
#     print(2+"")
# except Exception as error:
#     print({"failed to execute":error})
# else:  ##only executes if there are no errors
#     print("else block")
# finally:
#     print("it will always execute")



##Module:
# it is defined as a file containing functions, methods, variables
#it provides readability 

#module can be used anywhere by importing/exporting 


#there are 3 types of modules 
#1. built - in modules 
#math, re ,time ,os ,random 

#2 . custom /user defined modules 


#3.third party modules 
#pip  install   numpy ,pandas, matplotlib ,scikit


#funtion==> module ==> library ==>framework 
#flask , rest framework , django




import math 

# num=2.3
# print(num//1)

#floor()
#it round the decimal number to the nearest lowest integer
# print(math.floor(2.3))
# print(math.floor(5.0))
# print(math.floor(9.0))


#ceil
#it give the nearest highest integer to the decimal value
# print(math.ceil(3.01))
# print(math.ceil(6.3))
# print(math.ceil(6.0))


#pow
#it return the exponential value of the base and power 

# print(math.pow(53,2))
# print(math.pow(53,0))
# print(math.pow(53,-2)) 


#sqrt 
#it returns  the square root of the number 
# print(math.sqrt(25))
# print(math.sqrt(2500))
# print(math.sqrt(250))

# print(math.pi)
# print(math.e)


#factorial 
# n=7 
# # fact=1 * 2 * 3 * 4 * 5 * 6 *7
# # print(fact)
# print(math.factorial(7))

# fact=1
# for i in range(1,n+1):
#     fact=fact*i  #1*1   1*2  2*3 6*4  24*5  120*6  720*7
# print(fact)

#fmod
# print(math.fmod(10.5,3))

# print(10.5%3)
#

# print(math.remainder(14,4))


# print(math.isnan(22/7))

# print(math.isfinite(5))

# num=math.inf
# print(num)

# print(math.lcm(3,2))

# print(math.fabs(-2.3356))


# num=81
# sqrt=math.sqrt(num) ##5.91
# c_v=math.ceil(sqrt) ##6 

# if sqrt==c_v:
#     print(" perfect")
# else:
#     print(" not perfect")





# problem solving: 
# next nearest prime 

# num=2  #107
# nxt_prime_not_found=True
# while nxt_prime_not_found:
#     num=num+1  #104 105 106 107
#     fact=0 
#     for i in range(2,num):
#         if num%i==0:
#             fact+=1
#             break
#     if fact==0:  #1 1 1
#         print(f"next prime is {num}")
#         # break
#         nxt_prime_not_found=False



#fibanocci series 

#0 1 1 2 3 5 8 13 21 34 55 89 144.......

# limit=5
# a=0 
# b=1 

# for i in range(limit):
#     print(a) #
#     c=a+b #
#     a=b  #
#     b=c #


