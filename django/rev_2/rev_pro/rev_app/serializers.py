from rest_framework import serializers 
from .models import RevAppUsers


class USER_SERIALIZER(serializers.ModelSerializer):
    class Meta:
        model= RevAppUsers
        fields="__all__" 