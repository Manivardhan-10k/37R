from django.urls import path  
from . import views


#endpoint/url/api     #route--small portion of api
urlpatterns=[
    path("reg_user/",view=views.reg_user),
    path("login_user/",view=views.user_login),
]