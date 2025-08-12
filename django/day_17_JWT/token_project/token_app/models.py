from django.db import models

# Create your models here.

class USERS(models.Model):
    age=models.IntegerField()
    name=models.CharField(max_length=50,null=False)
    location=models.CharField(max_length=25)
    password=models.CharField(max_length=255)
    mobile=models.CharField(max_length=10,primary_key=True)
    is_admin=models.BooleanField(default=False)
