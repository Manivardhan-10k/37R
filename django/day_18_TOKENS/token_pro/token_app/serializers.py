from rest_framework import serializers 
from .models import USERS_DATA


class user_serializer(serializers.ModelSerializer):
    class Meta:
        model=USERS_DATA
        fields="__all__"
    