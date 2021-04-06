from django.shortcuts import render, redirect
from django.views.generic.list import ListView
from django.contrib.auth.models import User
from django.urls import reverse_lazy
from django.contrib.auth.views import LoginView, LogoutView
from django.views.generic.edit import CreateView
from .forms import AuthUserForm, RegisterUserForm
from django.contrib.auth import authenticate, login

from django.views.generic.base import TemplateView


class HomePageView(TemplateView):

    template_name = 'mainpage/home_page.html'

class UsersListView(ListView):
    model = User
    template_name = 'mainpage/users_list.html'
    context_object_name = 'users_list'


class MyProjectLoginView(LoginView):
    template_name = 'mainpage/login.html'
    form_class = AuthUserForm
    success_url = reverse_lazy('users')
    def get_success_url(self):
        return self.success_url


class RegisterUserView(CreateView):
    model = User
    template_name = 'mainpage/users_create.html'
    success_url = reverse_lazy('users')
    form_class = RegisterUserForm
    sucess_msg = 'Пользователь успешно создан'
    def form_valid(self, form):
        form_valid = super().form_valid(form)
        username = form.cleaned_data['username']
        password = form.cleaned_data['password']
        aut_user = authenticate(username=username, password=password)
        login(self.request, aut_user)
        return form_valid



class MyProjectLogout(LogoutView):
    next_page = reverse_lazy('users')

