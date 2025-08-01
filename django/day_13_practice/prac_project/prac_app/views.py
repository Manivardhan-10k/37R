from django.shortcuts import render
from .models import user 
from .serializers import userSerializer
from django.http import HttpResponse,JsonResponse
import json 
import bcrypt

# Create your views here.

#ORM
#Object Relational Mapping

def get_users(self):
    data=user.objects.all()
    serialize=userSerializer(data,many=True)
    return JsonResponse({"data":serialize.data}) 

def reg_user(self):
    req_data= json.loads(self.body) #to get the user data from req
    try:
     user_exists=user.objects.get(email=req_data["email"],mobile=req_data["mobile"])
     if user_exists:
        return HttpResponse("user exists with the email and mobile")
    except:
        pass
    password=req_data["password"].encode("utf-8") #user_123  to get password and change datatype
    salt=bcrypt.gensalt(12) #4-30  12 3 #to define how strong should be the password
    hashed_password=bcrypt.hashpw(password,salt)# creating  hashed password based on the salt
    req_data["password"]=hashed_password.decode("utf-8")# updating  the user data with hashed password
    serialize=userSerializer(data=req_data)    # validating the user data
    try:
     if serialize.is_valid():
        serialize.save()
        return JsonResponse({"result":serialize.data})
    except Exception as error:
        return JsonResponse({"error":error})
    return HttpResponse("failed to save the user")
    
def user_login(req):
    req_data=json.loads(req.body)
    user_exists=user.objects.get(email=req_data["email"]) 
    if  bcrypt.checkpw( req_data["password"].encode('utf-8'),user_exists.password.encode("utf-8")):
        return HttpResponse("login successful")
    else:
        return HttpResponse("invalid credentials")
    
    
