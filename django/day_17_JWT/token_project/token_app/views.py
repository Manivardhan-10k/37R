from django.shortcuts import render
from django.http import HttpResponse,JsonResponse
import json
from .serializers import userSerializer
import bcrypt
from django.views.decorators.csrf import csrf_exempt
from .models import USERS

import jwt

# Create your views here.

def users(req):
    return HttpResponse("app is working")

@csrf_exempt
def add_users(req):
  if req.method=="POST":
    user_data=   json.loads(req.body)
    user_password=user_data["password"] 
    user_password=user_password.encode("utf-8") 
    salt=bcrypt.gensalt(12)
    hashed_password=bcrypt.hashpw(user_password,salt)
    hashed_password=hashed_password.decode("utf-8")
    user_data["password"]=hashed_password
    serializer=userSerializer(data=user_data)
    if serializer.is_valid():
        serializer.save()
        return JsonResponse({"success":"data saved successfully"},status=201)
    else:
        return JsonResponse({"error":"failed to store data"},status=501)
  else:
      return JsonResponse({"error":"invalid method"},status=402) 
    

@csrf_exempt
def delete_user(req):
    user_data=json.loads(req.body)
    try:
        user_exists=USERS.objects.get(mobile=user_data["mobile"])
    except Exception as e:
        return JsonResponse({"error":"user not found"})
    else:
       if  user_exists.is_admin==True:
           try:
               user_tobe_deleted=USERS.objects.get(mobile=user_data["delete_mobile"])
           except :
               return JsonResponse({"error":"user to be deleted not found"})
           else:
               if user_tobe_deleted.is_admin==False:
                     user_tobe_deleted.delete()
                     return JsonResponse({"success":"user deleted successfully"})
               else:
                   return JsonResponse({"error":"you cannot delete a admin"})
       else:
           return JsonResponse({"error":"you are not authorized to delete"})       
    
##token 
