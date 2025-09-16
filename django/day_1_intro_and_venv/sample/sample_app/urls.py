from django.urls import path
from . import views

urlpatterns = [
    path("sample/",view=views.sample)
]