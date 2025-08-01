from django.urls import path 
from . import views

urlpatterns=[
    
    path("get_users/",view=views.get_users),
    path("reg_user/",view=views.reg_user),
    path("login_user/",view=views.user_login)
]