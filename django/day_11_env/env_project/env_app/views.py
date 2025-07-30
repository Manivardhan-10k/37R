from django.shortcuts import render 
from django.http  import HttpResponse,JsonResponse
from .serializers import StudentSerializer
from .models import Students
import json
# Create your views here.


def sample(request):
    return  HttpResponse("working")

def reg_stu(req):
  try:
    req_data=  json.loads(req.body)  
    serializer=StudentSerializer(data=req_data) 
    if serializer.is_valid():
        serializer.save()
        return HttpResponse("data saved successfully",status=201)
    return HttpResponse("invalid data")
  except Exception as e:
      return HttpResponse(f"{e}")


def get_students(req):
    stu_data=Students.objects.all()
    serializer=StudentSerializer(stu_data,many=True)
    return HttpResponse( f"working {serializer.data}") 

def getStudent(req,sid):
   try:
    stu_details=Students.objects.get(id=sid)
    serialize=StudentSerializer(stu_details)
    return JsonResponse({"data":serialize.data})
   except Exception as error:
       return HttpResponse(f"{error}")
      
    