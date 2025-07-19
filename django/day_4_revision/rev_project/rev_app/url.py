from django.urls import path   
from . import views

urlpatterns=[
    path("",view=views.home_page),
    path("greet/",view=views.greet),
    path("post/",view=views.only_post)
    
]