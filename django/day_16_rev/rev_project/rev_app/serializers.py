from rest_framework import serializers 
from .models import USERS

class userSerializer(serializers.ModelSerializer):
    class Meta:
        model=USERS 
        fields="__all__"
    