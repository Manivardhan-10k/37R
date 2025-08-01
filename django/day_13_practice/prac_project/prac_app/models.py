from django.db import models

# Create your models here.

class user(models.Model):
    id=models.IntegerField(primary_key=True)
    name=models.CharField(max_length=30,null=False)
    email=models.EmailField(max_length=50,unique=True)
    mobile=models.CharField(max_length=10,unique=True,null=False)  
    password=models.CharField(max_length=255)