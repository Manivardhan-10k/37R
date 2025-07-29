from rest_framework import serializers  
from .models import USERS

##Meta --> data about data
class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model=USERS
        fields=['id','name',"mob"]
        