from django.urls import path 
from .views import welcome

urlpatterns=[
    path("welcome/",welcome.as_view())
    ##path("route/",view=views.fun)
]