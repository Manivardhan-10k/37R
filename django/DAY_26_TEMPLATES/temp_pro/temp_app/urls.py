from django.urls import path
from .views import UserListView,UserDetailView,UserCreateView,UserUpdateView,UserDeleteView

urlpatterns=[
    # path("hi/",Mainview.as_view()),
    path("user_data/",UserListView.as_view(), name="user_data"),
    path('users/<int:pk>/', UserDetailView.as_view(), name='user-details'),
    path('users/add/', UserCreateView.as_view(), name='user-add'),
    path('users/<int:pk>/edit/', UserUpdateView.as_view(), name='user-edit'),
    path('users/<int:pk>/delete/', UserDeleteView.as_view(), name='user-delete'),
]