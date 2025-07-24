from django.db import models

# Create your models here.
class SampleTable(models.Model):
    name=models.CharField(max_length=50)
    password=models.CharField(max_length=20)
    mobile=models.CharField(max_length=10,default=0)



class Sample2(models.Model):
    id= models.IntegerField(primary_key=True)
    email=models.EmailField(max_length=50)