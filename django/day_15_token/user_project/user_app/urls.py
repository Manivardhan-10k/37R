from django.urls import path
from . import views

urlpatterns=[
    
    # path("got/",view=views.got),
    # path("list/",view=views.characters)
    path("reg_user/",view=views.reg_user),
    path("get_users/",view=views.get_users)
    
    
]