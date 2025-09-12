from django.urls import path 
from . import views
urlpatterns=[
    path("update/",view=views.update_user)
    
]