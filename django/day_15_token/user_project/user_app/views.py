from django.shortcuts import render
from django.http import HttpResponse,JsonResponse
import json
from django.views.decorators.csrf  import csrf_exempt
from .models import users
from .serializers  import usersSerializer

# Create your views here.

# def  got(req):
#     return HttpResponse("it is a english web series")

# def characters(req):
    
#     characters_list=['jon snow',"arya","tyrion","bryan"]
#     return JsonResponse({"list":characters_list})


@csrf_exempt
def reg_user(req): #json 
    if req.method=="POST":
     user_data=  json.loads( req.body) 
     new_user= users.objects.create(name=user_data["name"],mobile=user_data["mobile"])
     new_user.save()
     return HttpResponse("data saved successfully!")
     
    else:
        return HttpResponse("invalid method")
def get_users(req):
    users_data=users.objects.get()
    serialized_Data=usersSerializer(users_data)
    print(serialized_Data)
    return JsonResponse({"data":serialized_Data.data})
    




