# OOP:

# class : is a template/ blueprint for creating objects
# object : is an instance of a class
# inheritance : getting properties/values from  another class
# polymorphism :method behaving differently in  different class
# abstraction : hiding the implementation details
# encapsulation :combing all the properties and methods into a single unit

# l1=[1,2,3,4]
# print(type(l1))


# l2=list((1,2,3,4))
# print(type(l2))

# l1.append(5)
# print(l1)


# class vehicle:
#     type="vehicle"
#     def about(self):
#         return f"used for transport"
# cycle=vehicle()
# print(cycle)
# # print(vehicle.about())
# print(cycle.type)
# print(cycle.about())


# class Mobile:
#     brand="Apple"  #class property
#     def __init__(self,ram,screen,storage,battery,cam,processor):
#         print("hello from constructor")
#         self.ram=ram
#         self.screen=screen 
#         self.storage=storage 
#         self.capacity=battery
#         self.resolution=cam 
#         self.processor=processor

#     def about(self):
#         return (self.processor,self.resolution,self.screen,self.ram)
#         # return f"{self.brand} {self}"
        
# #constructor
# # is  a default method that is executed when a instance is created

# iphone1=Mobile("2gb","4inch","32gb","2000mah","8mp","a1") ## instance properties
# print(iphone1.about())

# iphone16=Mobile("16gb","6inch","512gb","5000mah","64mp","a18")
# print(iphone16.about())


# class  car:
    # airbags=True  ##class property
    # def details(this):
    #     return this
    # def about(self):
        # return f"this is a {self.company} car of {self.color} color of class {self.cat} made in {self.year} of {self.fuel} variant of price {self.prices[0][0]}lakhs"
    # def __init__(self,brand,color,type,year,variant,*args):
    #     print("instance created")
    #     self.company=brand
    #     self.fuel=variant 
    #     self.cat=type
    #     self.color=color   ##instance /object  variables
    #     self.year=year
    #     self.prices=args    ##([1,2,1.5,2])

# car1=car("tesla","white","super",2025,"electric",[1,2,1.5,2])
# car2=Car("tata","black","suv",2025,"diesel")
# print(car1.about())
# print(car1.airbags)
# car1=car()
# print(car1.details())

