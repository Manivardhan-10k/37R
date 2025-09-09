from django.urls import path 
from . import views

urlpatterns=[
    path("hello/",view=views.greeting),
    path("allusers/",view=views.all_users)
]