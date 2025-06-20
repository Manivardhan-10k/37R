# list
# dict 
# set / frozenset
# tuple 
# string 

#num 
#primitive 
#immutable
# int  
# # -infinity   0    infinity
# float 
# complex 


# print(type(0))
# print(type(-100))
# print(type(99855148))



# Float

# print(type(7.2))
# print(type(-7.2))
# print(type(5.0))


#complex
# print(type(2+5j))


# mob=9848022338

# mob=str(mob)
# print(type(mob))
# print(len(mob))

# Type conversion



#abs

# num=-123456
# print(abs(num))
# print(pow(5,3))
# #divmod 
# # print(divmod(5,2))

# qr=divmod(10,2)
# print(type(qr))
# quo=qr[0]
# rem=qr[1]
# print(quo,rem)


# print(5.1==5)


#even digits in the num


# mod  div

# num=123456789 # 123 12
# even_count=0
# while  num!=0: #123!=0    12!=0 1!=0  0!=0
#     last_digit=num%10  #3   2   1
#     if last_digit%2==0:
#         even_count+=1
#     # print(last_digit%2==0)  ##false true  false
#     num=num//10   #12.3  12       1.2  1        0.1  0
# print("there are ",even_count, " even digits in the number")




#find the length of the given number (no.of digits) without using type conversion 



#sum of even numbers
# num=789456123
# even_sum=0
# while num!=0:
#     last_digit=num%10 # 3  2 1 6 5 4 9 8 7
#     if last_digit%2==0: 
#         even_sum+=last_digit  #0+2  2+6 8+4  12+8
#     num=num//10#
# print(even_sum)



#find the primes in the number  



##  "mom"  -- "mom" 
# 12321  12321

# num=12121 # 121
# temp=num  #121
# rev=0 
# while num!=0: #123   12  1  0
#     last=num%10  #3  2  1
#     rev=  rev*10 +last   #0+3  30+2  320+1
#     num=num//10 # 12 1 0
# if rev==temp:
#     print("palindrome number")
# else:
#     print("not palindrome")



#Armstrong number 
#121 
#1**3 + 2**3 +1**3    1+8+1   10

#153
#1**3+5**3+3**3     1+125+27 153

##find the length 


# num=1634  # 1**4 +6**4 +3**4 +4**4     1+1296 +81 +216   1634
# temp=num
# temp2=num
# length=0
# while num!=0: #153  15 1
#      num=num//10 ##15 1 0
#      length+=1   #1 2 3
# total_sum=0
# while temp!=0:#153 15 1 0
#      last=temp%10  #3 5 1
#      total_sum= total_sum +  last**length  #27 27+125 152+1 
#      temp=temp//10# 15 1 0
# print(total_sum==temp2)
# #1234