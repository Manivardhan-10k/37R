##problem solving

# print(len(num))
# print(str(num)[3])


# num=1234   #length -4   length-1 3   length-2 2 length-3  1  
# temp=num #1234
# length=0
# pos=4
# while num>0:   #123 12 1 0
#     num=num//10   #12 1 0
#     length+=1  #1 2 3 4
# if length>=pos: #4>=4
#     while temp!=0:  #1234 123 12
#         digit=temp%10   #4 3 2
#         temp=temp//10  # 123 12 1
#         if length==pos:   ##4 == 2  3==2  2==2
#             print(digit) # 2
#             break
#         length-=1 # 3 2
# else:
#     print("not enough positions in the number")



#num=1234 True 

#find the digits are in ascending order or not
# num=12314
# prev=num%10 #4
# is_asc=True 
# while num!=0:#  12314 1231 123
#     digit=num%10 # 4 1 3
#     print(prev,digit)
#     if prev<digit: # 4<4 4<1 1<3
#         is_asc=False
#         break
#     prev=digit  # 4 1
#     num=num//10  # 1231 123
# if is_asc:
#     print("ascending order")
# else:
#     print("not ascending")


# num=9848022338 
# dig=8
# count=3 
# pos=10, 4, 2







