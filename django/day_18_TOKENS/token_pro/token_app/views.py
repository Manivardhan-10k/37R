from django.shortcuts import render
from django.http import HttpResponse,JsonResponse
import json
from .models import USERS_DATA
import bcrypt
import jwt
from .serializers import user_serializer
SECRET_KEY = 'django-insecure-ltp-3$%j2=mt*e-3l@m2b8m2nox_ir4hgm14pm#qbvfug0de!0'
# Create your views here.
def login(req):
    user_data=json.loads(req.body)
    user_exists=USERS_DATA.objects.get(mobile=user_data["mobile"])
    if user_exists:
        hashed=user_exists.password.encode("utf-8")
        password=user_data["password"].encode("utf-8")
        if bcrypt.checkpw(password,hashed):
                payload={
                   "name":user_exists.name ,
                   "password":user_exists.password,
                   "is_logged_in":True
                }        
                token=jwt.encode(payload,SECRET_KEY,algorithm="HS256")
                return JsonResponse({"msg":"login success!","data":token})
        
         
    

    
def get_users(req):
    user_data=json.loads(req.body)
    token=user_data["token"] 
    decoded=jwt.decode(token,SECRET_KEY,algorithms=["HS256"])
    if decoded["is_logged_in"]==True:
        all_users=USERS_DATA.objects.all()
        serialized=user_serializer(all_users,many=True)    
        return JsonResponse({"all data":serialized.data})
    else:
        return JsonResponse({"error":"login first"})
    
