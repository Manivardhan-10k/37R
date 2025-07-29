from django.urls import path 
from . import views


urlpatterns=[
    path("",view=views.welcome),
    path("regemp/",view=views.reg_employee),
    path("getemp/<int:id>",view=views.get_employee),
    path("updateemp/<int:emp_id>",view=views.update_emp)
]