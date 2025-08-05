from django.urls import path 
from . import views


urlpatterns=[
    path("users/",view=views.users),
    path("create_user/",view=views.create_user),
    path("update_user/",view=views.update_user),
    path("delete_user/",view=views.delete_user)
]