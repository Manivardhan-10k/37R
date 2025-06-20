# inheritance:
# class a:
#     class_var="class"

# class b(a):
#     class_var1="class2 "

# obj=b()
# print(obj.class_var1)
# print(obj.class_var) 

# obj2=a()
# # print(obj2.class_var1)


#polymorphism 
# class Dog:
#     def speak(self):
#         return f"barks"

# class Cat:
#     def speak(self):
#         return f"meows" 
    
# print(Dog().speak())
# print(Cat().speak())

class  Grand:
    def __init__(self,name):
        self.name=name

    def details(self):
        return f"hello , i am {self.name}"


class Parent(Grand): #class properties
    surname="something"
    def __init__(self,name):##instance properties
        self.name=name
    # def details(self):
    #     return f"my name is {self.name}" 

class Child(Parent):
    def __init__(self,name):
        self.name=name
    def details(self):
        return f" hi my name is {self.name}"
    
# p1=Parent("rao")
# print(p1.details())
# print(p1.surname)

c1=Child("mani")
print(c1.details())
