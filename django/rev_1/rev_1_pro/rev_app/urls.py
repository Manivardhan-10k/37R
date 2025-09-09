from django.urls import path 
from . import views


urlpatterns=[
    path("welcome/",view=views.welcome),
    # path("product/<int:id>/", view=views.get_product)
]