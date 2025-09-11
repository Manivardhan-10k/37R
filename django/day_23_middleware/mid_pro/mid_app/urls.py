from django.urls import path 
from . import views
urlpatterns=[
    path("data/",view=views.show_data)
]