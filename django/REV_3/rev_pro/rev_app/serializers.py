from rest_framework import serializers
from .models import RevAppUsers
class user_serializer(serializers.ModelSerializer):
    class Meta:
        model=RevAppUsers 
        fields="__all__"
        

