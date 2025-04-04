#fundementals 

#variables 
#datatypes 
#conditionals 
#loops 
#functions 


# l=[1,2,3]
# print(l[4])
# print("hi")

# age=int(input("enter the age: "))
# print("your age is ",age)
# print(5/0)


# Exception Handling Methods:

# Error:
# An error can be a problem in the syntax or logic



# try :
#it attempts to execute the block of code  
#except:
# it catches any errors and exceutes the code when try fails

# try:
#     #block of code
#     print("executed")
# except:
#     print("try failed")
# print("hi")
# print("hello")


# try:
#  age=int(input("enter your age: "))
#  print(age//0)
# except:
#   print("error")


# try:
#     l=[1,2,3]
#     # print(10/0)
#     print("hi"+1)
# except Exception as e:
#     print({"err" :e},Exception)


#else
#it only executes when there are no exceptions
# try :
#     sum=10/1
# except:
#     print("failed")
# else:
#     print(sum)


#finally
# try:
#     s1="hi"
#     n='hey'
#     t=s1+n
#     print(10/0)
# except Exception as error:
#     print(error)
# else:
#     print(t)
# finally:
#     print("this is excuted finally")




# error handling methods: 
# try
# except Exception as error
# else 
# finally


# String formatting
# name="mani"
# print("my name is  name")
# print(f"my name is  {name}")

# def greet(n,g):
#     return  f"hello {n} , {g} "
# print(greet("teja","good morning"))


# print(f"th sum of 2 , 3  is {2+3}")
# print(f"{10/0}")



#problem solving 
# string="Uday"  ##2 Vdby

# #65  - 90 
# #97 - 122 
# char="a"  #97 98 -b
# ascii_val=ord(char)+1
# next_char=chr(ascii_val)
# print(next_char)


# string="Uday"  ##Vdby
# res=""
# vowels="aeiouAEIOU"
# for i in string:
#     if i in vowels: #U d a
#          a_v= ord(i)
#          n_c=chr(a_v+1)
#          res=res+n_c ##Vdby
#     else:
#          res+=i #Vdby
# print(res)


#anagram 
# s1="studyi"
# s2="dustyi" 
# if len(s1)!=len(s2):
#     print("they are not anagrams")
# else:
#     ana=False
#     count=0
#     for i in s1: #t p
#         if s1.count(i)==s2.count(i): #1!==1 2!=1
#             count+=1
#     if count==len(s1):
#        ana=True
#     if ana:
#      print("anagram")
#     else:
#      print("not anagram")
