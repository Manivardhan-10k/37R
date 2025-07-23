from django.shortcuts import render 
from django.http  import HttpResponse,JsonResponse
from django.views.decorators.csrf  import csrf_exempt
from django.core.files.storage  import FileSystemStorage 
from . import products

# Create your views here.
# @csrf_exempt
# def sample(req):   
#     # print(req.method)
#     # print(req.GET) ## to get the queery params in the request
#     # print(req.POST) ## to get the form data (only works for form data)
#     # print(req.body) ## to get the json data
#     # print(req.headers)  ##to get the info of the request
#     # print(req.META) #
#     # print(req.path) # 
#     # print(req.path_info) #
#     # print(req.user)
#     # print(req.COOKIES)  #important
#     print(req.FILES["pic"])  
#     # print(req.session)
#     # print(req.scheme)
#     # print(req.encoding)  utf-8 
#     # print(req.content_type)
#     # print(req.content_params) 
#     if req.FILES["pic"]:
#        FileSystemStorage.url( FileSystemStorage.save(self=req.FILES["pic"],name="my_pic",content=req.FILES["pic"]))
        
         
    
#     return JsonResponse({"msg":"hello from siva"}) 


@csrf_exempt
def sample(req,ids):
    print(id)
    return JsonResponse({"id value":id})

@csrf_exempt 
def product(req,ids):
    if ids>=1 and ids<=20:
     for i in products.prod_list:
        if i["id"]==ids:
            return JsonResponse({"data":i})
    else:
        return JsonResponse({"error":"id should be between 1 and 20"})
            

    
    
    