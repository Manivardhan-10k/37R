from django.shortcuts import render
from django.http import HttpResponse
from .serializers import UserSerializer
import json


def update_user(req):
    user_data = json.loads(req.body)  # request body -> dict    
    user_instance = req.exist_data 
    serializer = UserSerializer(user_instance, data=user_data, partial=True)  
    if serializer.is_valid():
        serializer.save()
        return HttpResponse("Updated the user successfully!!")
    else:
        return HttpResponse(f"Invalid data: {serializer.errors}")