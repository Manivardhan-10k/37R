from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.


def show_data(req):
    return HttpResponse("welcome manivardhan ,from the view!")


