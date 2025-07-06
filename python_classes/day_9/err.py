##sys 
## version 
##sys path 
##platform 
##maxsize --32,64 
##module
##recursion  -- morespace  - 1000
##sys.stdin.readlines()
##sys.stdout




# error handling /exception handling 

#syntactical error  


#runtime 
#string /10 




# to buy an item 
# -> not going  //errors
#-> closed/item not available  exceptions





#exception handling methods 
# try 
# except 
# else 
# finally

# try: 
#     numerator=int(input("enter a number: "))
#     denominator=int(input("enter denominator: "))
#     result=numerator/denominator
# except Exception as something:
#     print(something)
# else:
#     print(result)
# finally:
#     print("i will irrespective of result")   
# print("division complete") 


# file=open("./sample.txt","x")
# print("file created")
# file=open("sample.txt","w")
# file.write("this content is added frm python code")
# print("wrote successsfully")

# try:
#     file=open("./sample.txt","r")
#     data=file.readline()
#     print(data)
# except Exception as err:
#     print("failed due to",err)
# finally:
#     file.close()
#     print("file is closed")
# print("file handling completed")
    
    
# LEGB 
# local 
# enclosed 
# global 
# built-in 

# a=20
# def outer():
#     global a
#     a=10
#     def inner():
#         global a
#         a+=5
#         print(a)
#     inner()
#     print(a)
# outer()
# print(a)
# LEGB

#parent scope --- non local 
##outside scope --global

