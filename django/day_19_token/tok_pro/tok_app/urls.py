from django.urls import path 
from . import views


urlpatterns=[
    path("get_token/",view=views.get_token)
]