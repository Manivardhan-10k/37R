# find the largest palindromic substring
# find the smallest palindromic substring 

            #row       cols
# * * * * *   1         5
# * * * * *   2         5
# * * * * *   3         5
# * * * * *   4         5
# * * * * *   5         5  
# rows=5 
# for row in range(rows): #0 1 2 3 4   --> for rows
#     s=""
#     for col in range(rows): #0 1 2 3 4  --->for columns 
#         s+="*"+" "  #*****
#     print(s)
    

        #    row          cols
#1 2 3 4 5  1               5
#1 2 3 4 5  2               5
#1 2 3 4 5  3               5
#1 2 3 4 5  4               5
#1 2 3 4 5  5               5

# rows=5 
# for row in range(rows):
#     string=""
#     for col in range(rows): #0 1 2 3 4  1 2 3 4 5
#         string+= str(col+1)+" "
#     print(string) 

#task -1
# 1 1 1 1 1
# 2 2 2 2 2
# 3 3 3 3 3
# 4 4 4 4 4
# 5 5 5 5 5


        #     row          cols
# 1            1             1
# 1 2          2             2
# 1 2 3        3             3
# 1 2 3 4      4             4
# 1 2 3 4 5    5             5 

# rows=5 
# for row in range(1,rows+1): #1 2 3 4 5
#     string=""
#     for col in range(1,row+1):##1 2 1
#         string += str(col)+" "
#     print(string)

#task -2
# 1
# 2 2
# 3 3 3 
# 4 4 4 4
# 5 5 5 5 5
