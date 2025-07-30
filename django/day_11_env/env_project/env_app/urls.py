from django.urls import path 
from . import views

urlpatterns=[
    path("",view=views.sample),
    path("regstu/",view=views.reg_stu),
    path("getstudents/",view=views.get_students),
    path("getstudent/<int:sid>",view=views.getStudent)
    
]