##strings 
# list 
# dict 
# set 
# patterns 


# * * * * *
# * * * * * 
# * * * * * 
# * * * * * 
# * * * * * 

# rows=5
# ##the first loop/outer  is for rows
# for i in range(1,rows+1): #1
#     row=""   #
#     for j in range(1,rows+1): #1 2 3 4 5
#         row+="*" +" "# *  * *   * * *    * * * *     * * * * *   
#     print(row)
    



# 1 1 1 1 1
# 2 2 2 2 2
# 3 3 3 3 3
# 4 4 4 4 4
# 5 5 5 5 5   

# rows=5 
# for i in range(1,rows+1):
#     res=""
#     for j in range(1,rows+1):
#         res+= str(i)+" "
#     print(res)    
    
# 1 2 3 4 5
# 1 2 3 4 5
# 1 2 3 4 5
# 1 2 3 4 5
# 1 2 3 4 5 



# *
# * *
# * * * 
# * * * * 
# * * * * * 

# rows=5
# for i in range(0,rows):
#     res=""
#     for j in range(0,i+1) : #1 2     1-3   1-4   1-5  1-6
#         res+="*"+" "
#     print(res)

# 1
# 2 2 
# 3 3 3 
# 4 4 4 4
# 5 5 5 5 5 

# 1
# 1 2
# 1 2 3
# 1 2 3 4
# 1 2 3 4 5

# 1 
# 2 3
# 4 5 6
# 7 8 9 10
# rows=4
# num=1
# for i in range(1,rows+1): #2
#     res=""
#     for j in range(1,i+1):
#         res+= str(num)+" " #1 2 2
#         num+=1 # 2
#     print(res)

# 1 
# 2 2
# 3 3 3
# 4 4 4 4