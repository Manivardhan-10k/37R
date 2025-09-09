from django.urls import path 
from . import views


urlpatterns=[
    path("sample/",view=views.sample),
    path("all_users/",view=views.all_departments),
    path("get_user/<int:id>",view=views.get_user)
]

##www.amazon.com/products   -- API
##              products ---route 


# relations  
# 1 -1     one user profile -- one user id
# 1- m     python     -- students
# m -m     students   -- subjects 





# existing 
# data 
# raw queries 
# sql injection 
# placeholders 

# relations