from django.shortcuts import render
from django.http import HttpResponse,JsonResponse
from django.views.decorators.csrf  import csrf_exempt

# Create your views here.


def home_page(request):
    return   JsonResponse({"msg":"WELCOME TO DJANGO"})  


def greet(request):
    return JsonResponse({"msg":"Good Morning From Django!"})

@csrf_exempt
def only_post(req):
    if req.method=="POST":
        return JsonResponse({"msg":"U R USING POST METHOD"})
    else:
        return HttpResponse(" INVALID HTTP METHOD")
    
