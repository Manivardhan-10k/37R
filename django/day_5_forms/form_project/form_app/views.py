from django.shortcuts import render
from django.http import HttpResponse,JsonResponse
from django.views.decorators.csrf import csrf_exempt
import json

# Create your views here.

name=""  #declaring variables for storing user values
pswrd=""
@csrf_exempt
def sample(req):
    return  HttpResponse("app is working")

# @csrf_exempt
# def handle_use_login_form_data(req):
#     if req.method=="POST":
#      global name,pswrd 
#      #POST --> form data submitted by client through request (it will be in dictionary)
#      name= req.POST.get("username")
#      pswrd=req.POST.get("password")
#      email=req.POST.get("email")
#      mobile=req.POST.get("mob")
#      dob=req.POST.get("dob")
#      print(name,pswrd,email,mobile,dob)
#      return JsonResponse({"msg":"data submitted successfully"})

#     else:
#         return JsonResponse({"msg":"invalid method for this endpoint"})
    

@csrf_exempt
def handle_user_login_form_data(req):
    # print(req.body) 
    #loads -->converts the json data into object form 
    # print(json.loads(req.body))
    user_data=json.loads(req.body)
    if user_data["username"] and user_data["password"]:
    
      return user_login(user_data["username"],user_data["password"])

def user_login(u,p): 
    if u=="manivardhan" and p=="secret":
        return HttpResponse("login successful")
    else:
        return HttpResponse("invalid credentials")
    


# dumps-->  object into json 
# loads --> json into object   

# get_data -->form data ()
# get_data--> json


    