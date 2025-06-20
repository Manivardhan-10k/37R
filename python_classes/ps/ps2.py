# "aaabbc" #a3b2c1 
# s="heloh"
# sub="heli"

# # print(sub in s) 
# exists=False
# for i in range(len(s)): #0
#     if s[i]==sub[0] and   len(s)-i >=len(sub):  # h ==h   h==h
#         if sub==s[i:i+len(sub)]:   #s[0:0+4]   helo  heli==helo   heli==h
#             exists=True
# print(exists) 


# string="programming" # hel   low  world
# longest="" #hel low  world
# for i in range(len(string)):
#     temp=""
#     for j in range(i,len(string)):  
#         if string[j] not in temp:
#             temp+=string[j] 
#             print(temp)   
#         else:
#             break
#     if len(temp)>len(longest):
#         longest=temp
# print(longest)

# find the largest palindromic substring in a string

# string="world"
# #racecar aceca cec 
# longest=""
# for i in range(len(string)):
#     temp=""
#     for j in range(i,len(string)):
#         temp+=string[j] #racecar
#         if  temp==temp[::-1] and len(temp)>len(longest):
#             if len(temp)>2:
#                longest=temp
# if longest:
#     print(longest)
# else:
#     print("no palindromic substrings")


