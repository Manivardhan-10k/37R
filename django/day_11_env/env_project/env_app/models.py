from django.db import models

# Create your models here.

class Students(models.Model):
    #variable ==fields 
    id=models.IntegerField(primary_key=True)
    stu_name=models.CharField(max_length=50)
    stu_batch=models.IntegerField(null=False)