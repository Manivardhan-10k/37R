#requests module 

#request  - API/endpoint/url
# server -   

import requests as req   ##
import json 


##http methods 
##get post put/patch delete

# data=req.get("https://fakestoreapi.com/products")
# print(data.status_code)  ###respose code 
# print(data.json())    ##json format
#1xx  -info 
#2XX  -- success msg
#3XX-- rederictional msgs
#4XX -- client side errors
#5XX  -- server side errrors


##forms --fields --->server



# details={"id":"3","name":"kalyn"}
# ##dumps 
# details=json.dumps(details)

# data=req.post(url="http://localhost:3000/users",data=details)
# print(data.status_code)


##put  -- it replaces the entire record with new values

# details={"id":"3","name":"kalyan"}

# data=req.put(url="http://localhost:3000/users/3",json=details)
# print(data.status_code)


# details={"id":"3","name":"sanjay","batch":"37r"}
# details=json.dumps(details)
# head={"Content-Type":"Application/json"}
# data=req.put(url="http://localhost:3000/users/3",data=details,headers=head)
# print(data.status_code)
# print(data.json())  

#patch

# details={"batch":"35r"}
# data=req.patch(url="http://localhost:3000/users/1",json=details)
# print(data.status_code)
# print(data.json())


##delete 
# data=req.delete(url="http://localhost:3000/users/3")
# print(data.status_code)
# print(data.json())


base_api="http://localhost:3000/users/"

# inp=input("enter the input in order(name,batch): ")
# det=inp.split(" ") ##["name","batch"]
# details={"name":det[0],"batch":det[1]}
# data=req.post(url=base_api,json=details)
# print(data.status_code)
# print(data.json())  


# data=req.patch(url= f"{base_api}9a29",json={"batch":"35r"})
# print(data.status_code)
# print(data.json())
# try:
#     data=req.delete(url=f"{base_api}9a29")
# except Exception as err:
#     print(f"failed due to {err}")
# else:  
#   print(data.status_code)
#   print(data.json())
# print("deleted successfully")



#get  
#post
#update
#delete  


# get  post update delete

