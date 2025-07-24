from django.urls import path 
from . import views


urlpatterns=[
    path("sample/",view=views.sample),
    path("postdata/",view=views.post_data),
    path("getdata/",view=views.get_users)
    
]