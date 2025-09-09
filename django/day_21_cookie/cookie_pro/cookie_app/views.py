from django.shortcuts import render
from .serializers import abcd 
from .models import cookie_user
import json
from django.http import HttpResponse,JsonResponse 
import bcrypt
from django.views.decorators.csrf import csrf_exempt

# Create your views here.

@csrf_exempt
def register(req):
    #username    password  mobile email  age 
     user_data= json.loads(req.body)
     user_password=user_data["password"].encode("utf-8")
     salt=bcrypt.gensalt(12)
     hashed_password=bcrypt.hashpw(user_password,salt)
     hashed_password=hashed_password.decode("utf-8")
     user_data["password"]=hashed_password
     serialized_data=abcd(data=user_data) 
     if serialized_data.is_valid():
         serialized_data.save()
         response= JsonResponse({"success":"user registered successfully!"})
         response.set_cookie(   
            key="is_registered",
            value=True,
            max_age=60 ,
            secure=False,
            samesite="None"    
            )    
         return response
     else:
         return HttpResponse("incorrect data!")

         