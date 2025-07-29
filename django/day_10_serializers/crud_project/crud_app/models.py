from django.db import models

# Create your models here. 
class USERS(models.Model):
    id=models.IntegerField(primary_key=True)
    name=models.CharField(max_length=30,null=False,default="user")
    mob=models.CharField(max_length=10,unique=True)
