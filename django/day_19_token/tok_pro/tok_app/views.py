from django.shortcuts import render
from django.http import HttpResponse,JsonResponse
import jwt
from datetime import datetime,timedelta

# Create your views here. 

SECRET_KEY = 'hello from python'
user_details={
    "name":"kalyan",
    "batch":"37",
    "is_admin":False,
    "exp":datetime.utcnow()+timedelta(seconds=5),
    "iat":datetime.utcnow()
}

jwt_token=jwt.encode(user_details,SECRET_KEY,"HS256") 
print(jwt_token)


# decoded_token=jwt.decode(jwt_token,SECRET_KEY,algorithms=["HS256"])
# print(decoded_token)





def get_token(req):
    print(req.COOKIES)
    return  JsonResponse({"data":jwt_token})




