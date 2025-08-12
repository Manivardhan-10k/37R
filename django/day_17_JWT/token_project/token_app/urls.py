from django.urls import path 
from . import views

urlpatterns=[
    path("users/",view=views.users),
    path("add_users/",view=views.add_users),
    path("delete_user/",view=views.delete_user)
]