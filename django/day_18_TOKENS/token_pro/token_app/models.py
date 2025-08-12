from django.db import models

# Create your models here.

class USERS_DATA(models.Model):
    mobile=models.CharField(max_length=10,primary_key=True)
    password=models.CharField(max_length=255)
    name=models.CharField(max_length=30,null=False)