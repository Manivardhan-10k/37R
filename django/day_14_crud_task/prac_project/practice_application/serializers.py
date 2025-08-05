from rest_framework import serializers 
from .models  import user_data
##model    normal  
class user_serializer(serializers.ModelSerializer):
    class Meta:
        model=user_data 
        fields="__all__"