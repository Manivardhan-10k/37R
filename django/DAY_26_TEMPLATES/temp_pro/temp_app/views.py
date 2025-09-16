from django.shortcuts import render
from django.views import View
from django.http import HttpResponse 
from django.views.generic import ListView, DetailView,CreateView,UpdateView,DeleteView
from .models import PracAppUser
from django.urls import reverse_lazy
# Create your views here.


# class Mainview(View):
#     def get(self,req):
#         return HttpResponse ("from get")

class UserListView(ListView):
    model = PracAppUser
    template_name = 'user_list.html'
    context_object_name = 'users'

class UserDetailView(DetailView):
    model = PracAppUser
    template_name = 'user_details.html'
    context_object_name = 'users'
    
    
# Create a new user
class UserCreateView(CreateView):
    model = PracAppUser
    template_name = 'user_form.html'
    fields = ['id', 'name', 'email', 'mobile', 'password']
    success_url = reverse_lazy('user_data')
    
class UserUpdateView(UpdateView):
    model = PracAppUser
    template_name = 'user_form.html'
    fields = ['name', 'email', 'mobile', 'password']
    success_url = reverse_lazy('user_data')
    
    
class UserDeleteView(DeleteView):
    model = PracAppUser
    template_name = 'user_delete.html'
    context_object_name = 'user'
    success_url = reverse_lazy('user_data')