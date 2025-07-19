import requests ,json

url="http://127.0.0.1:8000/post/" 


# data=requests.get(url=url)
# print(data.json())  

data=requests.post(url=url)
print(data.json())

