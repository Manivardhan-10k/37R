from django.shortcuts import render 
from django.http import HttpResponse,JsonResponse 
import json
from django.views.decorators.csrf  import csrf_exempt 
from .models  import EMPLOYEE
# Create your views here.


def welcome(req):
    return  HttpResponse("app is working")  


@csrf_exempt
def reg_employee(req):
    # all_record=EMPLOYEE.objects.all()
    # print(all_record)
    
    data=   json.loads(req.body) 
    print(data)
    new_emp=EMPLOYEE.objects.create(
        emp_name=data["name"], 
        emp_mob=data["mob"], #
        emp_email=data["email"] ,#
        id=data["id"], ##
    )
    print(new_emp) 
    return HttpResponse("emp created",status=201)   

def get_employee(req,id): 
    if id:
     employee=EMPLOYEE.objects.get(id=id)
     print(employee.id)
     print(employee.emp_name)
     print(employee.emp_mob)
     print(employee.emp_email)

     return JsonResponse({"msg":"user found" ,"data":dict(employee)})
    else:
        return HttpResponse ("user not found")


def update_emp(req,emp_id):
    emp=EMPLOYEE.objects.get(id=emp_id)   ## get - to get the record based on the condition
    
    data=json.loads(req.body) #  to get the values from the request   ##dictionary
    
    if data["name"]:
        emp.emp_name=data["name"]  ##updating the existing value with new value
        emp.save() # to make  the changes permanant
    return HttpResponse ("emp updated")
    

    
        
         
    
    
    
    
    
    
    
     
    
    
    