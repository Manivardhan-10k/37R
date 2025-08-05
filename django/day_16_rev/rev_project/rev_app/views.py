from django.shortcuts import render
from django.http import HttpResponse,JsonResponse
from .serializers import userSerializer
from .models import USERS
import json
from django.views.decorators.csrf import csrf_exempt
import bcrypt
# Create your views here.

##create hashed password 

def create_hashed_password(password):  #ramesh
    #for hashing the password 
    password=password.encode("utf-8")
    salt=bcrypt.gensalt(12)
    hashed_password=bcrypt.hashpw(password,salt) 
    hashed_password=hashed_password.decode("utf-8")
    return hashed_password
    
def users(req):
    users_data=USERS.objects.all() 
    serialized_data=userSerializer(users_data,many=True)
    return JsonResponse({"data":serialized_data.data}) 



@csrf_exempt
def create_user(req):
    user_data=  json.loads( req.body)
    user_data["user_password"]=create_hashed_password(user_data["user_password"])
    serialized_data=userSerializer(data=user_data)
    if serialized_data.is_valid():
        serialized_data.save()
        return JsonResponse({"msg":"user created successfully"})
    else:
        return JsonResponse({"error":"failed to create user"})

def update_user(req):
  user_data= json.loads(req.body)
  if user_data["user_password"]:
     user_data["user_password"]=create_hashed_password(user_data["user_password"])
  try:
    user_exist=USERS.objects.get(user_mobile=user_data["user_mobile"])
  except Exception as e:
        return JsonResponse({"error":"user not found"})
  else:
    if user_exist:
     serialized_data=userSerializer(user_exist,data=user_data,partial=True)
     if serialized_data.is_valid():
        serialized_data.save()
        return JsonResponse({"msg":"user updated successfully"})
     else:
        return JsonResponse({"msg":"failed to update user"})
    
def delete_user(req):
    user_data=json.loads(req.body)
    user_exists=USERS.objects.get(user_mobile=user_data["user_mobile"])
    if user_exists:
        user_exists.delete()
        return JsonResponse({"msg":"user deleted successfully"})
    else:
        return JsonResponse({"error":"user not found"})


# JWT-json web token