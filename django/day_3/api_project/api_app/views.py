from django.shortcuts import render
from django.http import HttpResponse ,JsonResponse

from django.views.decorators.csrf  import csrf_exempt

# Create your views here.


# @api_view
#get post put patch delete

# @csrf_exempt  ##to allow all the http methods
# def welcome(req):
#     method=req.method
#     if method=="GET":
#         return HttpResponse(f"you are using {method} method")
#     elif method=="POST":
#         return HttpResponse(f"you are using {method} method")
#     elif method=="PUT":
#         return HttpResponse(f"you are using {method} method")
#     elif method=="PATCH":
#         return HttpResponse(f"you are using {method} method") 
#     else:
#         return HttpResponse(f"you are using {method} method") 
        
        
        


# CORS -- Cross Origin Resource Sharing
# CSRF 

#     post: 
#     put 
#     patch
#     delete 

# @csrf_exempt
# def get_view(req):
#     return HttpResponse("get view") 
# @csrf_exempt
# def post_view(req):
#     return HttpResponse("post view") 
# @csrf_exempt
# def put_view(req):
#     return  HttpResponse("put view")
# @csrf_exempt
# def patch_view(req):
#     return  HttpResponse("patch view")

# @csrf_exempt
# def delete_view(req):
#     return  HttpResponse("delete view") 
# @csrf_exempt
# def deflt(req):
    
#     print(req )
#     return HttpResponse("you're successfully connected to the server")
