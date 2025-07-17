from django.shortcuts import render
from django.http import HttpResponse,JsonResponse

# Create your views here.


##function based view 


def test(self):
    # return HttpResponse("welcome to django")
    return JsonResponse({"msg":"app is working","code":"200"})