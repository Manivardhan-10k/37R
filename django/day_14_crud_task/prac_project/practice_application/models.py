
from django.db import models

# Create your models here.
class user_data(models.Model):
    user_id=models.IntegerField(primary_key=True) 
    user_name=models.CharField(max_length=30)
    user_password=models.CharField(max_length=255)
    user_mobile=models.CharField(max_length=10,unique=True)
    
