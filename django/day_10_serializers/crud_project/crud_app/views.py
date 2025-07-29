from django.shortcuts import render
from django.http  import HttpResponse,JsonResponse
from django.views.decorators.csrf import csrf_exempt
import json
from .models import USERS
from .serializers import UserSerializer
# Create your views here.


def get_users(req):
    users=USERS.objects.get()
    updated_data=UserSerializer(users)
    return  JsonResponse({"data":updated_data.data})
@csrf_exempt
def reg_user(req):
    data=json.loads(req.body)  
    user_data=UserSerializer(data=data)    
    if user_data.is_valid():
         print("user data is valid")
         user_data.save() 
    print("after the validataion")
    # new_user=USERS.objects.create(
    #     id= data["id"],
    #     name=data["name"],
    #     mob=data["mob"]     
    # )
    return JsonResponse({"msg":"success user created"},status=201)
    
def delete_user(req,id):
    user=USERS.objects.get(id=id)
    user.delete()
    return HttpResponse("user deleted successfully")