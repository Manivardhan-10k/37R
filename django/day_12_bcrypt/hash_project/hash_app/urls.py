from django.urls import path 
from . import views

urlpatterns=[
    path("reguser/",view=views.reg_user),
    path("getuser/",view=views.user_login)
]