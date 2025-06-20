# * * * * *
# * * * * * 
# * * * * * 
# * * * * * 
# * * * * *  


# 1 1 1 1 1 
# 2 2 2 2 2
# 3 3 3 3 3
# 4 4 4 4 4  
# 5 5 5 5 5 

# 1
# 2 2
# 3 3 3
# 4 4 4 4
# 5 5 5 5 5

          # rows   col
# 1         1       1
# 2 3       2       2
# 4 5 6     3        3
# 7 8 9 10  4        4 

# rows=4 
# count=1

# for i in range(1,rows+1):#1 2 3 4
#     res=""
#     for j in range(1,i+1) : #1  2   3  4
#         res+=str(count)+" "    ## 1   2 3  4 5 6  7 8 9 10
#         count+=1  #2 3 4 5 6 7 8 9 10 11
#     print(res)
# print(count)






  
               #rows   col
# a              1      1
# b c            2      2
# d e f          3      3
# g h i j        4      4
# k l m n o      5      5
# rows=5 
# code=97

# for i in range(rows):##0 1 2 3 4 
#     res=""
#     for j in range(i+1): #
#         res+= chr(code)+" " ##a 
#         code+=1
#     print(res)




# * * * * *
# *       *
# *       *
# *       *
# * * * * * 

# rows=5
# for i in range(1,rows+1):#0 1 2 3 4
#     res=""
#     for j in range(1,rows+1):#1 2 3 4 5
#         if i==1 or j==1 or i==rows or j==rows:
#             res+="*"+" " # * * * * *
#         else:
#             res+=" "+" "
#     print(res)






# *
# * *
# *   *
# *     *
# * * * * *


# rows=5 
# for i in range(1,rows+1):
#     res=""
#     for j in range(1,i+1):
#         if j==1 or i==rows or i==j:
#             res+="*"+" "
#         else:
#             res+=" "+" "
#     print(res)

# X O X O X
# O X O X O 
# X O X O X 
# O X O X O 
# X O X O X 


#11  13 15 
# 22 24
#31 33 35 
#42 44 
#51 53 55
# rows=5
# for i in range(1,rows+1): 
#     res=""
#     for j in range(1,rows+1):
#         if (i+j)%2 ==0:
#             res+="X"+" "
#         else:
#             res+="O"+" "
#     print(res) 




# a 
# b c 
# d   f 
# g     j 
# k l m n o 