from django.urls import path 
from . import views

urlpatterns=[
    path("welcome/",view=views.welcome),
    path("getusers/",view=views.get_users),
    path("postuser/",view=views.post_user),
    path("patchuser/<int:id>",view=views.patch_user)
]