from rest_framework import serializers 
from .models import cookie_user

class abcd(serializers.ModelSerializer):
    class Meta:
        model=cookie_user
        fields="__all__"