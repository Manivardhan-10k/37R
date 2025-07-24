from django.shortcuts import render
from django.http import HttpResponse,JsonResponse
import json
from django.views.decorators.csrf import csrf_exempt
from .models import SampleTable
# Create your views here.

user_data=[]
def sample(req):
    return  HttpResponse("working") 


@csrf_exempt
def post_data(req): 
    data=json.loads(req.body)
    user_data.append(data)
    print(user_data)
    return HttpResponse ("data submitted")


def get_users(req):
    all_users=SampleTable.objects.first()
    # for i in all_users:
    #     print(i.name)
    print(all_users.password)
    
    return HttpResponse("getting all users")
    
