from django.shortcuts import render, redirect
from django.views.generic.list import ListView
from django.contrib.auth.models import User
from django.urls import reverse_lazy
from django.contrib.auth.views import LoginView, LogoutView
from django.views.generic.edit import CreateView, DeleteView, UpdateView
from .forms import AuthUserForm, RegisterUserForm, UserUpdateForm
from django.contrib.auth import authenticate, login
from django.contrib import messages
from django.contrib.messages.views import SuccessMessageMixin

from django.views.generic.base import TemplateView


class HomePageView(TemplateView):

    template_name = 'mainpage/home_page.html'

class UsersListView(ListView):
    model = User
    template_name = 'mainpage/users_list.html'
    context_object_name = 'users_list'


class MyProjectLoginView(SuccessMessageMixin, LoginView):
    template_name = 'mainpage/login.html'
    form_class = AuthUserForm
    success_url = reverse_lazy('home')
    success_message = 'Вы залогинены'
    def get_success_url(self):
        return self.success_url


class RegisterUserView(SuccessMessageMixin, CreateView):
    model = User
    template_name = 'mainpage/users_create.html'
    success_url = reverse_lazy('login_page')
    form_class = RegisterUserForm
    success_message = 'Пользователь успешно создан'



class MyProjectLogout(SuccessMessageMixin, LogoutView):
    next_page = reverse_lazy('users')
    success_message = 'Вы разлогинены'


class DeleteUserView(DeleteView):
    model = User
    success_url = reverse_lazy('users')
    template_name = 'mainpage/delete_user.html'


class UpdateUserView(UpdateView):
    model = User
    template_name = 'mainpage/user_update_form.html'
    form_class = RegisterUserForm
    success_url = reverse_lazy('users')