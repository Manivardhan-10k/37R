from django.shortcuts import render
from django.http import HttpResponse,JsonResponse
import json
import jwt

# Create your views here.

username="manivardhan"
password="secret"
SECRET_KEY = 'django-insecure-jr!h7^*%$2z0q$2%@f!t1frid_e3t3yi-n-+@joj5+827dm7%+'

def login(req): 
    # data=json.loads(req.body)
    # name=data["name"]
    # password=data["pass"]
    # if name==username and password==password:
        payload={
            "username":username,
            "is_logged_in":True
        } 
        token=jwt.encode(payload=payload,key=SECRET_KEY)
        response=JsonResponse({"msg":"login successful!"})
        response.set_cookie(key="login_token",value=token,max_age=120,httponly=True)
        return response
    # else:
    #         return HttpResponse("invalid credentials")
        
def products(req):
    try:
    #    req.COOKIES["login_token"]
       token=req.COOKIES["login_token"]
       data=jwt.decode(token,SECRET_KEY,algorithms=["HS256"])
       if data["is_logged_in"]==True:
          return JsonResponse({"products":"laptop"})
       else:
          return HttpResponse("pls login to view products")
    except:
        return HttpResponse("invalid token/no token")
    

        

    
    
    
    