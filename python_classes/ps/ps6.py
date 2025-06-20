#  * * * * * 
#  *       *
#  *   *   *
#  *       *
#  * * * * * 

# rows=5 
# mid=rows//2  + 1
# for i in range(1,rows+1):
#     res=""
#     for j in range(1,rows+1):
#         if i==1 or i==rows or j==1 or j==rows or i==mid and j==mid:
#             res+="*"+" "
#         else:
#             res+=" "+" "
#     print(res)


 
            #    row    col        space
#     *           1      1           4
#    * *          2      2           3
#   * * *         3      3           2
#  * * * *        4      4           1
# * * * * *       5      5           0
##rows= 5  i= 1     4
# rows=5 
# for i in range(1,rows+1):#1
#     res=""
#     for sp in range(rows-i): #  
#         res+=" "
#     for j in range(1,i+1) :  #1   
#         res+="*"+" "
#     print(res)


          #rows       j        i
# 5 4 3 2 1  1        5        5      
# 4 3 2 1    2        4        4
# 3 2 1      3        3        3
# 2 1        4        2        2
# 1          5        1        1


# rows=5 
# for i in range(rows,0,-1):  ##5 4 3 2 1
#     res=""
#     for j in range(i,0,-1):  ## 5 4 3 2 1   4 3 2 1  3 2 1  2 1 1
#         res+=  str(j)  +" "
#     print(res)



# task#1
# 5 5 5 5 5
# 4 4 4 4
# 3 3 3 
# 2 2
# 1 



#task2
          #    i    j     space
# * * * * *    1    5      0
#  * * * *     2    4      1
#   * * *      3    3      2
#    * *       4    2      3
#     *        5    1      4 


## i-1     1-1 0     2-1 1    3-1 2  4-1  3   5-1   4





# * * * * *
# *
# *
# * * * * *
# *
# *
# * * * * *

# rows=7
# mid=rows//2 +1

# for i in range(1,rows+1):#1 2 3 4
#     res=""
#     for j in range(rows-2):#0 1 2 3 4
#         if i==1 or i==rows or i==mid or j==0:
#             res+="*"+" "  ## * * * * *
#     print(res)


# *       *
#   *   *
#     *
#   *   *
# *       *

# rows=5 

# for i in range(rows):
#     res=""
#     for j in range(rows):
#         if i==j or i+j==rows-1:
#             res+="*"+" "
#         else:
#             res+=" "+" "
#     print(res)

# * * * * *
#     *
#     *
#     *
# * * * * *

# rows=5 
# mid=rows//2 +1 
# for i in range(1,rows+1):
#     res=""
#     for j in range(1,rows+1):
#         if i==1 or i==rows or j==mid:
#             res+="*"+" "
#         else:
#             res+=" "+" "
#     print(res)


#task3
# *       *
# *       *
# * * * * *
# *       *
# *       *

# j==1 or j==rows or i==mid




# 7-5-2025


       #     rows   col
# * * * * *   1      5
# *           2      1
# * * * * *   3      5
#         *   4      1
# * * * * *   5      5


# rows=9
# mid=rows//2 +1
# for i in range(1,rows+1):#1 2 3 4
#     res=""
#     for j in range(1,rows+1):##1 2 3 4 5
#         if i<mid: ##1<3 2<3
#             if i==1 or j==1: ##
#                 res+="*"+" "  ##* 
#         elif i>=mid: ##3>=3  4>=3
#             if i==mid or i==rows or j==rows: ##
#                 res+="*"+" " ## 
#             else:
#               res+=" "+" "
#     print(res)




# *
# * *
# * * * 
# * * * *
# * * * * *

# * * * *
# * * *
# * *
# *

# rows=5 
# for i in range(1,rows+1):
#     res=""
#     for j in range(1,i+1):
#         res+="*"+" "
#     print(res)

# for i in range(rows-1,0,-1):  #4 3 2 1
#     res=""
#     for j in range(1,i+1):  #1 ,5
#         res+="*"+" "
#     print(res)




#         *
#       * *
#     * * *
#   * * * *
# * * * * *
    
       #rows     i      j
#   * * * *      4      4 
#     * * *      3      
#       * *
#         *

# rows=5 
# for i in range(1,rows+1):
#     res=""
#     for j in range(1,rows+1):
#         if i+j>=rows+1:
#             res+="*"+" "
#         else:
#             res+=" "+" "
#     print(res)

# for i in range(rows-1,0,-1):##4
#     res=""
#     for j in range (1,rows+1):##1 2 3 4 5 
#         if i+j >rows:
#             res+="*"+" "
#         else:
#             res+=" "+" "
#     print(res)




            #    row    col        space
#     *           1      1           4
#    * *          2      2           3
#   * * *         3      3           2
#  * * * *        4      4           1
# * * * * *       5      5           0    
#  * * * *        4      4           1
#   * * *         3                  2
#    * *          2                  3
#     *           1      1           4

# rows=5 
# for i in range(1,rows+1):
#     res=""
#     for sp in range(rows-i):
#         res+=" "
#     for j in range(1,i+1):
#         res+="*"+" "
#     print(res)
# for i in range(rows-1,0,-1):#4 3 2 1
#     res=""
#     for sp in  range(rows-i):
#         res+=" "
#     for j in range(1,i+1):
#         res+="*"+" "
#     print(res)



##teranary operator 
## it is a shorthand notation of writing if else statement 

# n1=10 
# n2=20 
# min=0
# if n1<n2:
#     min=n1
# else:
#     min=n2 
# print(min)
# min=n1 if n1<n2 else n2 
# print(min)

# num=15 
# even="odd" if num%2!=0 else "even" 
# print(even)


# *       *
# * *     * 
# *   *   * 
# *     * *
# *       *



# * * * * * 
#     *
#     *
# *   * 
# * * *



# * * * * *
# *       *
# * * * * * 
# *   *
# *       *





# 8-5-2025 



     #           i           j
# *              1           1
# * *            2           2
# * * *          3           3
# * * * *        4           4
# * * * * *      5           5
# * * * *        6           4
# * * *          7           3
# * *            8           2
# *              9           1

# rows=5
# for i in range(1,2*rows):##1 2 3 4 5 6 7 8 9 
#     res=""
#     cols=i if i<=rows else 2*rows-i    ##rows5   i6     j4
#     for j in range(1,cols+1):
#         res+="*"+" "
#     print(res)



     ##            i      j      sp
#    *             1      1       3
#   * *            2      2       2
#  * * *           3      3       1
# * * * *          4      4       0
#  * * *           5      3       1
#   * *            6      2       2          
#    *             7      1       3
# rows=int(input("enter the rows: "))
# for i in range(1,2*rows): ## 1 2 3 4 5 6 7
#     res=""
#     spaces= rows-i  if i<=rows else i-rows
#     cols=i if i<=rows else 2*rows-i 
#     for sp in range(1,spaces+1):
#         res+= " "
#     for j in range(1,cols+1):
#         res+="*"+" "
#     print(res)




#hour glass pattern 
         #            i       j     spaces
#      * * * * *      1       5      0 
#       * * * *       2       4      1
#        * * *        3       3      2
#         * *         4       2      3
#          *          5       1      4
#         * *         6       2      3
#        * * *        7       3      2
#       * * * *       8       4      1
#      * * * * *      9       5      0


# rows=5         ##rows 5    i6   i-rows+1 9-5+1
# #          5-1+1  5-2+1
# for i in range(1,2*rows): ##1,9
#     res=""
#     space= i-1 if i <=rows else 2*rows-i-1  ##0  1 2 3 4 3 2 1 0
#     cols=  rows-i+1 if i<=rows else i-rows+1  ##5 4 3 2 1 2 3 4 5
#     for sp in range(1,space+1):
#         res+=" "
#     for j in range(1,cols+1):
#         res+="*"+" "
#     print(res)



     ##            i      j      sp
#    *             1      1       3
#   * *            2      2       2
#  *   *           3      3       1
# *     *          4      4       0
#  *   *           5      3       1
#   * *            6      2       2          
#    *             7      1       3 


# rows=int(input("enter the rows: "))
# for i in range(1,2*rows):##1 2 3 4 5 6 7
#     res=" "
#     spaces= rows-i if i<=rows else i-rows 
#     cols= i if i<=rows else 2*rows-i 
#     for sp in range(1,spaces+1):
#         res+=" "
#     for j in range(1,cols+1):
#         if j==1 or j==cols:
#           res+="*"+" "
#         else:
#             res+=" "+" "
#     print(res)

# * * * * *
# *       *
# * * * * * 
# *   *
# *       *  

# rows=5 
# mid=rows//2 +1
# for i in range(1,rows+1):
#     res=""
#     for j in range(1,rows+1):
#         if i<=mid:
#             if i==1 or i==mid or j==rows or j==1:
#                 res+="*"+" "
#             else:
#                 res+=" "+" "  
#         else:
#             if j==1 or i==j:
#                 res+="*"+" "
#             else:
#                 res+= " "+" "
#     print(res)






# 10-5-2025


# a 
# b e 
# c f h
# d g i j
##a1  b2 c3 d4 e5 f6 g7 h8 i9 j10

# rows=4
# for i in range (1,rows+1):#1 2 3 4
#     res=""
#     n=i #1 2 3 4
#     for j in range(1,i+1): ##1  12 123 1234
#         res+= chr(96+n)+" " ##a be  cfh  d
#         n+=rows-j  ##9+4-3
#     print(res) ##a be





# 1 
# 2 5
# 3 6 8
# 4 7 9 10

# rows=4 
# for i in range(1,rows+1):
#     res=""
#     n=i
#     for j in range(1,i+1):
#         res+= str(n)+" "
#         n+=rows-j
#     print(res)
        
        

#         1
#       1 2 1
#     1 2 3 2 1
#   1 2 3 4 3 2 1 

# rows=4 

# for i in range(1,rows+1):
#     res=""
#     for sp in range(rows-i):
#         res+=" "+" "
#     for j in range(1,i+1):
#         res+= str(j)+" "
#     for j in range(i-1,0,-1):
#         res+= str(j)+" "
#     print(res)
    







