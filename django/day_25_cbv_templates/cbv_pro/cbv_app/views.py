from django.shortcuts import render
from django.http import HttpResponse,JsonResponse 
from django.views import View
from django.views.decorators.csrf import csrf_exempt
import json
## cross site request forgery 

# Create your views here.

# def welcome():
#     pass

class NextMixin:
    def dispatch(self,req):
        user_Data= json.loads(req.body)
        if not user_Data["next"]:
            return HttpResponse("cant proceed to login mixin")
        return super().dispatch(req)
class LoginRequiredMixin:
    def dispatch(self, request):
        user_data=json.loads(request.body)
        if not user_data["logged_in"]:
            return HttpResponse("You must log in first! from mixin", status=401)
        return super().dispatch(request) 


class welcome(LoginRequiredMixin,NextMixin,View): ##MRO
    def get(self,req):
        return HttpResponse ("response from get view after login" )
    @csrf_exempt    
    def post(self,req):
        return HttpResponse("from the post view")
    def patch():
        pass 
    def put():
        pass 
    def delete():
        pass
    



##user validation in fbv --> req.cookies.get("token name")

##middleware 

##mixin
## forget password -> user id ->otp 
##change password  -> prev pass + otp 
## registation  -> details+ otp

##callback



##MRO - method resolution order



    
    
# class animal:
#     def sound(self):
#         return "makes sound"
    
# class dog:
#     def sound(self):
#         return "barks"
    
# class tommy(dog,animal):
#     pass 

# t1=tommy()
# t1.sound()



