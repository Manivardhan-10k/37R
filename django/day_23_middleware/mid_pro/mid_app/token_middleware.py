import jwt
from django.http import JsonResponse
from django.conf import settings
import json

class JWTAuthenticationMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        # token = request.COOKIES["token_name"]

        # if not auth_header or not auth_header.startswith("Bearer "):
        #     return JsonResponse({"error": "Authorization header missing"}, status=401)

        # token = auth_header.split(" ")[1]
        if  len(request.COOKIES.keys())==0:
            return JsonResponse({"msg":"token is missing","msg2":"from the middleware"})
        else:
            token = request.COOKIES["token_name"]

        try:
            payload = jwt.decode(token, settings.SECRET_KEY, algorithms=["HS256"])
            request.user = payload.get("user")
        except jwt.ExpiredSignatureError:
            return JsonResponse({"error": "Token expired"}, status=401)
        except jwt.InvalidTokenError:
            return JsonResponse({"error": "Invalid token"}, status=401)

        response = self.get_response(request)
        return response 
    
    
class NameMiddleware:
    names=[n]
    def __init__(self,get_response):
        self.get_response=get_response 
    
    def __call__(self, req):
        user_data=  json.loads( req.body)
        user_name=user_data["name"]
        if user_name=="Manivardhan":
                   response = self.get_response(req)
                   return response 
        else:
            return JsonResponse({"msg":"who r u?","text":"from the middleware"})
        