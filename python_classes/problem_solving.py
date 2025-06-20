#list
# set/frozenset 
# dict 
# tuple 
# strings 

# name="kUshAl"  #u a
# # name=name.lower()
# vowels="aeiouAEIOU" 
# v_c=0
# c_c=0
# for i in range(0,len(name),1):
#     # if name[i] =="a" or name[i]=="e" or name[i]=="o" or name[i]=="u" or name[i]=="i":
#     #     v_c+=1
#     # else:
#     #     c_c+=1
#     if name[i] in  vowels: ## in works as membership operator
#         v_c+=1
#     else:
#         c_c+=1


# print("there are ",v_c, "vowels in the name")
# print("there are ",c_c, "consonants in the name")


# string=input("enter the string : ") #hello  0 1 2 3 4
# #olleh 
# # len -1
# rev=""
# for i in range (len(string)-1,-1,-1):
#    rev += string[i]

# if string==rev:
#    print("palindrome")
# else:
#    print('not palindrome')
# #palindrome
# #mom  dad sis madam wow malayalam racecar  


# 1- 100

# for i in range(1,100+1,1):
#     print(i)



# name="RAKesh"  #rakESH
# # print(name.swapcase())
# new=""
# for i in range(0,len(name),1):
#     if name[i].isupper(): #R
#       new+=  name[i].lower() #r
#     else:
#        new+= name[i].upper()
# print(new)


# string="this is a string in python" #4
# # print(string.replace("i","I"))
# new=""
# count=0
# for i in range(len(string)): ##t 
#     if string[i] =="i" and count==0:
#         new=new+string[i].upper()
#         count+=1 #1
#     else:
#         new+=string[i]
# print(new)  #thIs is a 


# para="python is a object oriented programming language"
# print("there are ",len(para.split(" "))," words in the sentence")

# inp=input("Enter the numbers seperated by ,: ")
# out=inp.split(",")
# print(out)

# word="hello"
# l=[]
# for i in range(len(word)):
#     l.append(word[i])
# print("".join(l))

# l2=list(word)
# print(l2)

# l3=[i     for i in word       if i in "aeiou" ]
# print(l3)


# para="10k coders for 10k coders learning python in 10k coders" #for learning python in
# wl=para.split(" ") ##to get the words in the string in the list
# for i in range(len(wl)):
#     w=wl[i] ## to store the single word
#     if wl.count(w)==1: #
#         print(w)


# word="ProgrammING"  ##uc=4  lc=7   65-90   97-122 ord()
# #code =101    
# #if code>=97 and code<=122