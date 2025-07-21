from django.urls import path  
from . import views

urlpatterns=[
    path("sample/",view=views.sample),
    path("get_data/",view=views.handle_user_login_form_data)
]