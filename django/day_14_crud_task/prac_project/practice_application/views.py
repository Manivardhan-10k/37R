from django.shortcuts import render
from django.views.decorators.csrf   import csrf_exempt
from django.http import HttpResponse,JsonResponse
import json
from .serializers import user_serializer
import bcrypt
from .models import user_data

# Create your views here.

@csrf_exempt
def reg_user(req):
    if req.method=="POST": 
        req_data= req.body
        req_data= json.loads(req_data)
        #### to hash the password 
        user_password=req_data["user_password"] ##mani@123 
        user_password=user_password.encode('utf-8')## to convert into byte code       
        ##to create salt 
        salt=bcrypt.gensalt(12) ## to define how strong a password should be
        hashed_password=bcrypt.hashpw(user_password,salt)
        hashed_password=hashed_password.decode("utf-8")##to convert byte code into string
        ##change the user_password with hashed password 
        req_data["user_password"]=hashed_password
        serialized_data=user_serializer(data = req_data)
        if serialized_data.is_valid():
           serialized_data.save()   
           return JsonResponse({"success":"user data is registerd"})
        else:
            return JsonResponse({"error":"failed to register user"})
    else:
        return  HttpResponse("invalid method")
    
    
def user_login(req):
    data=req.body   ##to get the user data
    data=json.loads(data)  ## to convert user data into python objects
    try:## to handle the risky code of finding the user
     user_exist=user_data.objects.get(user_mobile=data["user_mobile"])
     if user_exist:
      password_match= bcrypt.checkpw(data["user_password"].encode('utf-8'),user_exist.user_password.encode('utf-8'))    
      if password_match:
        return JsonResponse({"msg":"login successful"})
      else:
        return JsonResponse({"msg":"invalid credentials"}) 
    except:
        return HttpResponse("user not found")  
    
    
    #req--->json   -->python (json.loads)
    #db->queryset  -->python (serializer)