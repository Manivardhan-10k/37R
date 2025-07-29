from django.db import models

# Create your models here. 
class EMPLOYEE(models.Model):
    id=models.IntegerField(primary_key=True)
    emp_name=models.CharField(max_length=100,null=False,default="employee")
    emp_mob=models.CharField(max_length=10,unique=True)  
    emp_email=models.CharField(max_length=50,unique=True)
    
    
    
