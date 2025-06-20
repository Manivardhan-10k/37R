# oops: 
# class 
# object /instance 
# constructor 

# class variable 
# instance variables 



# class CelloPen:
#     brand="cello"  #class variable 
#     def __init__(self,color,type):
#         print("new pen is created")
#         self.color=color  #instance variable
#         self.type=type    #instance variable 
#     def details(self):
#         return {f"color":self.color}


# pin_point=CelloPen("blue","ball point")
# print(pin_point.brand)
# print(pin_point.color)
# print(pin_point.type)


# reynolds=CelloPen("red","gel")
# print(reynolds.brand)
# print(reynolds.color)
# print(reynolds.type)
# print(reynolds.details())



class Animal:
    speak=False 
    def explain(self):
        return f"i am a animal"

class Dog(Animal):   ##extending a class  Dog-child class  Animal - parent class
    sound="bark"
    def __init__(self,breed,name):
        self.breed=breed 
        self.name=name 



class Myra(Dog):
    food=""


    


