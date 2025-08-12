from django.urls import path 
from . import views


urlpatterns=[
    path("set_cookie/",view=views.setCookie),
    path("getCookie/",view=views.getCookie),
]