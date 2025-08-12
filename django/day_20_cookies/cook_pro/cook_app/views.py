from django.shortcuts import render
from datetime import datetime,timedelta
import jwt
from django.http  import HttpResponse,JsonResponse

# Create your views here.


payload={
    "name":"madhu","batch":"35",
    "exp":datetime.utcnow() + timedelta(minutes=30),
    "iat":datetime.utcnow() ,
    "is_logged_in":True
}
SECRET_KEY = 'django-insecure-eukgn!i780leh^_k1ftv8uqj_u0gj-4f^enx8a*h5^#7$=rr@p'
token=jwt.encode(payload,SECRET_KEY,algorithm="HS256")

def setCookie(req):
    response=  JsonResponse({"msg":"success"})
    response.set_cookie(key="json_token",value=token)
    return response

def getCookie(req):
    user_token=req.COOKIES["json_token"]
    is_valid=jwt.decode(user_token,SECRET_KEY,algorithms=["HS256"])
    if is_valid["is_logged_in"]:
        return HttpResponse ("Welcome to the APP")
    else:
        return HttpResponse("Pls login to  continue")
    
    
    



