# list 
# string 
# dict 
# tuple 
# set 
 


# zip: it combines values from several iterables/collection
# names=("vikas","madhu","udayasree","mani")
# num=["9848022338","8125579630","7843246548","4654589789","5645647821"]

# # for i in range(len(names)):
# #     print((names[i],num[i]))

# final=zip(names,num)
# print(list(final)) 

# num=[0,-1,-2,-3]
# print(any(num))

# 21_4_2025
# zip
# t1=(1,2,3,4,5,6)
# t2=(7,8,9,10,11,12)
# t3=(13,14,15,16,17,18)
# out=zip(t1,t2,t3)
# out=list(out)
# print(out)


# any
# l1=[0,None,False,"",[],{},()]
# print(any(l1))

# all 
# l2=[1,2,3,4,5,6,7,8,9,10]
# print(all(l2))


# map :
# it is used to iterate over the list and it returns new object based on the condition
# l=[1,2,3,4,5,6,7,8,9,10]
# out=map(lambda item :item*5,l)
# out=map(lambda ele:ele%2==0,l)
# out=map(lambda ele:ele-1,l)

# def div(ele=0):
#     return ele//2
# out=map(div,l)
# out=list(out)
# print(out)
# print(l)



# filter: 

# tech=["python","java","c++","c#","html","javascript","css","git"]
# out=filter(lambda ele: "c" in ele,tech)
# out=list(out)
# print(out)


# details=[{"name":"shankar","marks":95},{"name":"kalyan","marks":80},{"name":"teja","marks":99}] 
# out=filter(lambda ele: ele["marks"]>80,details)
# out=tuple(out)
# print(out)


# names=["shankar","kalyan","teja","chery","suryaaa","himabindhu"]
# names.sort(key=lambda x : len(x))
# print(names)


# nested=[[1,2],[-9,40],[2,9],[0,2]] ##12 02 29 -9 40
# nested.sort(key=lambda ele:ele[1])
# print(nested) 


# \n --for new line

# num=[1,2,3,4,5,6,7,8,9,10]
# for i in num:
#     print(i,end="\t")

# print("hello\rworld")

# print("python is \n \"great\"")


# num=12945
# #middle elements are greater than the first ele or not 
# even=len(str(num))%2==0
# first=str(num)[0]
# first=int(first)
# if even:
#     mid1=len(str(num))//2   ##3
#     mid2=len(str(num))//2 -1 ##2 
#     if int(str(num)[mid1])>first and int(str(num)[mid2])>first:
#         print("valid")
#     else:
#         print("invalid")
# else:
#     mid=len(str(num))//2
#     if int(str(num)[mid])>first:
#         print("valid")
#     else:
#         print("invalid")

# string="abracadabra" #abrakadabra
# ind=string.index("c") 
# char="k"
# string=list(string)
# string[ind]=char 
# string="".join(string)
# print(string)