from rest_framework import serializers 
from .models import PracAppUser



class  UserSerializer(serializers.ModelSerializer):
    class Meta:
        model=PracAppUser
        fields="__all__"