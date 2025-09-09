from django.urls import path 
from . import views

urlpatterns=[
    path("login/",view=views.login),
    path("products/",view=views.products)
    
]