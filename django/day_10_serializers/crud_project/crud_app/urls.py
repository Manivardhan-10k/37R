from django.urls  import path 
from . import views



urlpatterns=[
    path("getusers/",view=views.get_users),
    path("reguser/",view=views.reg_user),
    path("deluser/<int:id>",view=views.delete_user)
]