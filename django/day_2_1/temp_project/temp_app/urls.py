from django.urls import path   
from . import views


urlpatterns=[
    path("test/",view=views.test)
]