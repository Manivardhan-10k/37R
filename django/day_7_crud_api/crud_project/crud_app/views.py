from django.shortcuts import render
from django.http import HttpResponse ,JsonResponse
from . import users
from django.views.decorators.csrf import csrf_exempt
import json

# Create your views here.

def welcome(req):
    return HttpResponse("welcome to CRUD app")
##CRUD 
##READ 
user_data=users.user_list

@csrf_exempt
def get_users(req):
    if req.method=="GET" :
        if len(user_data)>0:
            return JsonResponse({"data":user_data})  
            return HttpResponse(f"{user_data}")
        else:
            return JsonResponse({"msg":"there are no users"})
    else:
        return HttpResponse("invalid method")
    

@csrf_exempt
def post_user(req): 
    if req.method=="POST":
        reg_data=json.loads(req.body)
        try:
         if reg_data["username"] and reg_data["password"] and reg_data["email"] and reg_data["mobile"]:  
            details={
                "id":len(user_data)+1,
                "username":reg_data["username"],
                "password":reg_data["password"],
                "email":reg_data["email"],
                "mobile":reg_data["mobile"]
            }  
            user_data.append(details)    
            return HttpResponse("user registered successfully",status=201)
        except:
            return HttpResponse("missing required fields")
    else:
        return HttpResponse("invalid method")     


@csrf_exempt
def patch_user(req,id):
    if req.method=="PATCH":     
        # return HttpResponse ("patch method")
        data=json.loads(req.body) 
        user_exists=False
        for i in user_data:
            if i["id"]==id:  
                user_exists=True       
                i["password"]=data["password"]
                return HttpResponse("password updated")
        if user_exists==False:
            return HttpResponse("no user found",status=404)       
        
        
        