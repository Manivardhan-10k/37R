
from .models import PracAppUser 
import json
from django.http import JsonResponse



class UserExistMiddleware:
    def __init__(self,get_response):
        self.get_response=get_response
    def __call__(self,req):
        user_data=json.loads(req.body)
        try:
           exist_user= PracAppUser.objects.get(mobile=user_data["mobile"])
           if exist_user:
               req.exist_data=exist_user
        except:
            return JsonResponse({"msg":"no user found with this mobile","src":"middleware"})
        
        response=self.get_response(req) 
        return response
            
        