from django.db import models

# Create your models here. 

class USERS(models.Model):
    user_name=models.CharField(max_length=30)
    user_mobile=models.CharField(max_length=10,unique=True)
    user_email=models.EmailField(max_length=50,unique=True)
    user_password=models.CharField(max_length=255,default=None)
    
