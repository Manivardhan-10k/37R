# file handling methods 
# seek 
# to move the cursor to certain place 

#tell 
#to know where the cursor is

# truncate:  
# it reduces tthe data to a given size

#flush 
#to write the chnages immediatly to the disk 
 
# with open() as file:
#     file.read()
     




# modules:
# prewritten code 

# function 

# same file 

# from module import method/variable/class
# import sample as s
# import greeting as gt 


# print(s.msg)
# print(s.say_hi("mani"))
# print(gt.mrng("raviteja"))

import math as m 

# print(m.sqrt(49))  7.0
# print(m.sqrt(50.23)) 7.023558
# print(m.sqrt(121))  11.0



# print(m.ceil(10.23))
# print(m.ceil(10))
 
 
##floor 
# print(m.floor(10.23))
# print(m.floor(10.99999)) 


# x=81
# y=m.sqrt(x) #10.2365
# if m.floor(y)==y:
#     print(" perfect square") 
# else:
#     print("not perfect square")

# **
# print(m.pow(2,-3))
# print(m.pow(5,10))


# print(m.fabs(-3))
# print(m.fabs(3))

# print(m.factorial(5))
# print(m.factorial(10))


##greatest common divisor 
# 20 16  
# 4
# print(m.gcd(20,4))
# print(m.gcd(13,39))


# print(m.log(5))
# print(m.log10(5))
# print(m.log2(5))


# print(m.pi)
# print(m.e)
# print(m.lcm(6,12))
# print(m.lcm(5,7))
# print(m)



# sqrt 
# pow **
# factorial 
# fabs 
# ceil 
# floor 
# gcd 
# lcm 

# pi


# print((49)**0.5)




# * * * * *
# *       *
# *       *
# *       *
# * * * * *

# rows=5 
# for i in range(1,rows+1): ##1 2 3 4 5
#     res=""
#     for j in range(1,rows+1): #1 2 3 4 5
#         if i==1  or i==rows  or j==1 or j==rows:
#             res+="*"+" "
#         else:
#             res+=" "+" "
#     print(res)
    
    
    
# * * * *
# *      
# *      
# *      
# * * * *
# rows=5 
# for i in range(1,rows+1):
#     res=""
#     for j in range(1,rows):
#         if i==1 or i==rows or j==1:
#             res+="*"+" "   
#     print(res)


# *       *
#   *   *
#     *
#   *   *
# *       *

# rows= 5 
# for i in range(1,rows+1):
#     res=""
#     for j in range(1,rows+1):
#         if i==j or i+j==rows+1:
#             res+="*"+" "
#         else:
#             res+=" "+" "
#     print(res)

# * * * * 
# *
# * * * * 
# *
# * * * * 

# rows=5 
# # rows//2+1
# for i in range(1,rows+1):
#     res=""
#     for j in range(1,rows):
#         if i==1 or i==rows or j==1 or i==(rows//2)+1:
#             res+="*"+" "
#     print(res)  

 
# *       *
# * *     *
# *   *   *
# *     * *
# *       * 

# * * * * * 
#       * 
#     * 
#   * 
# * * * * *  

# *       *
# *       *
# * * * * *
# *       *
# *       * 

# * * * * *
#     *
#     *
#     *
# * * * * * 



