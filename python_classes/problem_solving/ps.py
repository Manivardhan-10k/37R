# strings 
# numbers 
# list 
# dict


#palindrome 


# word="malayalam" 

# ## omom
# # print(word==word[::-1])
# rev=""
# last=len(word)-1 
# for i in range(last,-1,-1):  ##start stop-1 step
#     rev=rev+word[i] #""+s+ so som somo somom
# if word==rev:
#     print("palindrome")
# else:
#     print("not palindrome")


# if sub in word:
#     print(True)
# else:
#     print(False)
# word="sports"
# sub="ports"

##check sub string is a part of given string or not 

# found=False
# for i in range(len(word)):   
#     for j in range(len(sub)):
#         if sub[j]==word[i]:
#           if sub == word[i:i+len(sub)+1]:
#            print(True)
#            found=True
#            break
#     if found:
#         break 
# if found==False:
#     print("not found")
    
            
##longest palindromic substring 

word="aabbcbbaa" #abbcbba
longest=""#0 1
for i in range(len(word)):##0
    temp=""
    if len(longest)>len(word[i::]):
        break
    for j in range(i,len(word)):  ##0
        temp+=word[j]  ## aa          
        if temp==temp[::-1] and len(temp)>len(longest):
            longest=temp  #a  aa
print(longest)
    

            
        
