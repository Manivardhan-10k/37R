from django.urls import path 
from . import views

urlpatterns=[
    
    path("login_user/",view=views.login),
    path("get_users/",view=views.get_users)
]