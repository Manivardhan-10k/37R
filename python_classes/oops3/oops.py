# oops:
# classes 
# objects 
# inheritance 
# polymorphism 

# encapsulation 
# abstraction

# class animal:
#     cate="animal" #class variable
#     __breed="shepard"
#     def __init__(self,name):
#         self.name=name
#         #private variable 
#         #protected variable

#     def about(self):
#         return f"this is a animal {self.__breed}"

# dog=animal("jimmy")
# print(dog.name)
# print(dog.about())
# print(dog.cate)
# print(dog.__breed)


# abstraction:
# hiding the implementation and showing what is necessary


# decorators 
# @

# def my_decorator(func):
#     def wrapper():
#         func()
#         print("this is the first line")
#         print("this is after wrapper")
#     return wrapper

# @my_decorator
# def say_hi():
#     print("hi ,this is python") 
# say_hi()




# a=10  #10
# b=10 
# a=a+1  #11




# print(id(a),id(b)) 


# garbage collection:


# l1=[[1,2],[3,4]]
# l2=[[1,2],[3,4]]


# l1=[[1,2],[3,4]]
# l2=l1.copy()#[[1,2],[3,4]]




# print(id(l1[1][0]),id(l2[1][0]))


# def f1():
#     print("hi")


# def f2():
#     print("hi")
# def f3():
#     print("hi")



# print(id(f1),id(f2),id(f3))

# a=10 
# b="hi"
# c=True
# print(id(a),id(b),id(c))

# garbage collector: 
#reference counter 






s="aaaabbbzzzzzvvvegh"  #a4b3z5v3e1g1h1
n=s[0] #a
c=0
res=""
for i in range(len(s)): #a 
    if s[i]==n : # a==a  a==a  a==a b==a b==b
        c+=1  #1 2 3  2
    if s[i]!=n:
        res+=n+str(c) #a3
        n=s[i] #b
        c=1 #1
    if s.index(s[i])==len(s)-1:
       res+=n+str(c)  
print(res)
