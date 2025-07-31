from django.db import models
from datetime import datetime

# Create your models here.
class users(models.Model):
    id=models.IntegerField(primary_key=True)
    name=models.CharField(max_length=50)
    password=models.CharField(max_length=255)
    mob=models.CharField(max_length=10)
    reg_on=models.DateTimeField(blank=True ,default=datetime.now())
    