from django.shortcuts import render
from django.http import HttpResponse,JsonResponse
import json
from .serializers import userSerializer 
from .models import users
import bcrypt

# Create your views here.

def reg_user(request): 
    #json / form data 
    
    req_data=json.loads(request.body) 
    
    password=req_data["password"].encode("utf-8")
    #h ->i->j ->k>l>m>n   4-32   10-12
    salt=bcrypt.gensalt(12)
    hashed_password=bcrypt.hashpw(password,salt).decode("utf-8")
    req_data["password"]= hashed_password
    # print(req_data,hashed_password)
    # details=users.objects.create(
    #     id=req_data["id"],
    #     name=req_data["name"],
    #     mob=req_data["mob"],
    #     password=req_data["password"],
    # ) 
    # return JsonResponse({"msg":"user data saved successfully"},status=201)
    serialize=userSerializer(data=req_data)
    try: 
     if serialize.is_valid():
        serialize.save()
        return JsonResponse({"msg":"user data saved successfully"},status=201)
    except Exception as e:
        return JsonResponse({"msg":e})
    
def user_login(req):
    data = json.loads(req.body)
    try:
        user = users.objects.get(name=data["name"])
    except users.DoesNotExist:
        return JsonResponse({"error": "User not found"}, status=404)
    same = bcrypt.checkpw(
        data["password"].encode("utf-8"),
        user.password.encode("utf-8")
    )
    print(same)
    if same:
        return HttpResponse("Login successful")
    else:
        return JsonResponse({"error": "Invalid password"}, status=401)
    
    
    