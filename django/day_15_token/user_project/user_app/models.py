from django.db import models

# Create your models here.
class users(models.Model): ##inheriting /accessing  properties in the parent in child class
    name=models.CharField(max_length=30)
    mobile=models.CharField(max_length=10,unique=True)
    