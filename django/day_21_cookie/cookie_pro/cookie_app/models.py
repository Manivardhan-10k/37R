from django.db import models

# Create your models here.

class cookie_user(models.Model):
    username=models.CharField(max_length=50)
    password=models.CharField(max_length=255)
    email=models.EmailField(max_length=40,unique=True)
    age=models.IntegerField()
    mobile=models.CharField(max_length=10,unique=True,null=False)