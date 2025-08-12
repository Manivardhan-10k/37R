##pyJwt 


import jwt  

##encryption 

data={
    "name":"manivardhan",
    "city":"hyd",
    "mobile":"9848012399"
}

key="this is my key" 
key2="this is the duplicate key"
my_token=jwt.encode(data,key)
print(my_token) 
decoded=jwt.decode(my_token,key,algorithms=["HS256"])
print(decoded)