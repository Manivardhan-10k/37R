from django.urls import path 
from . import views

urlpatterns=[
    # path("sample/<int:id>",view=views.sample) 
    path("product/<int:ids>",view=views.product)
]