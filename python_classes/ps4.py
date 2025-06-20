# scope:
# the possibility to access the variable/value

# LEG: 
# Local:
# within the function block 
# def hi():
#     val=10 
#     print(val)
# hi()
# print(val)
# Enclosed: 
# def outer():
#     count=100  
#     def inner():
#         nonlocal count
#         count+=100
#         print(count)#200
#     inner()
# outer()

# Global:
# val=10 
# def v():
#     global val
#     val=val+10
#     print(val)
# v()

# nonlocal 
# global 


# PS:  

# fizz/buzz
# 3 -fizz 
# 5- buzz 
# 3,5 -fizzbuzz
# 1-100
# 1.iterate  from 1 -100 
# 2.we need to check whether is multiple of 3 or 5 or both
# 3.print the values
# for i in range(1,101,1): # 
#     if i%3==0 and i%5==0:
#         print("fizz buzz")
#     else:
#         if i%3==0:
#          print("fizz")
#         if i%5==0:
#          print("buzz")
#         else:
#            print(i)


    # if i%3!=0 and i%5!=0 :
    #     print(i)


# for  i in s2: ##mani vardhan 
#     res=""
#     for j in i:#m
#         if i.index(j)==0:
#            res+=j.upper()
#         else:
#             res+=j
#     final+=res+" "
# print(final)
# for i in range(len(s2)):
#     res=""
#     for j in range(len(s2[i])):
#         if j==0:
#            res+=s2[i][j].upper()
#         else:
#             res+=s2[i][j]
#     s2[i]=res
# final=" ".join(s2)
# print(final)
# string="5mani vardhan"  #Mani Vardhan
# s2=string.split(" ")
# final=""
# for i in s2:#mani vardhan
#     res=""
#     if i[0].isalpha():
#        res=i[0].upper()# M V
#        res+=i[1::] #Mani Vardhan
#     else:
#         res+=i
#     final+=res+" "#5mani Vardhan 
# print(final.strip())

# name="harsha"  ## hbrshb 
# count={}
# sentence="dont trouble the trouble"#
# for i in sentence:
#     if not i.isspace():
#      count[i]=sentence.count(i)
# c=0 
# max=""
# for i in count:
#    if count[i]>c:
#       c=count[i]
#       max=i
# print(max,c)
sen="ntng is permenant"
mid=len(sen)//2
first=sen[:mid+1:]
second=sen[mid+1::]
f_v=0 
s_v=0
vowels="aeiou"
for i in first:
    if i in vowels:
        f_v+=1
for i in second:
    if i in vowels:
        s_v+=1
if f_v>s_v:
    print(first, "has more vowels")
elif s_v>f_v:
    print(second,"has more vowels")
else:
    print("both has same no of vowels")

