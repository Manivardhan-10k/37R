# exception handling 
# runtime errors -exception  

#methods 
# try -- we write the code 
# except -- handles the errors /exceptions 
# except Exception as exception/name:

#else: -- only if the try is executed/if there is no exception 

#finally -- excecutes irrespective of result 




#modules 
# they are python files containing functions variables classes

# import module 

# print(module.fun())


#built-in 
# math random os sys datetime
#user defined 
# they are created by users


#third party
# they are installed from internet

#requests
# API --> Application Programmin Interface


# package managers
#PIP   --->"pip installs packages"
# pip install package_name

import requests,json


# 1  inforamtional codes
# 2  success
# 3   redirectional
# 4    client side error
# 5     server side error

# data=requests.get("https://fakestoreapi.com/products")
# print(data.status_code)  ##response codes
# for i in data.json():
#     print(i["title"])


# users=requests.get("http://localhost:3000/users")
# print(users.status_code)
# print(users.json()) 
# ser_url="http://localhost:3000/users"
# sen_data={"name":"javascript"}#python dict
# sen_data=json.dumps(sen_data) ## converting the python dict into json string
# posting=requests.post(url=ser_url,data=sen_data)
# print(posting.status_code)


# data=requests.get(ser_url)
# print(data.json())



# url="http://localhost:3000/languages"
# s_data={"name":"RUST"}
# send_data=requests.post(url=url,json=s_data) ##json keyword is used to convert the datatype automatically
# print(send_data.status_code)
# print(send_data.json())



#requests 
#pip install requests 

#get  --for getting data
#post  -- for sending data    dumps()    ## keyword(json)

# 200 
# 400 
# 500