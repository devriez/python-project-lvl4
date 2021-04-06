from django.contrib import admin
from django.urls import path, include
import django.contrib.auth.urls
from .views import UsersListView, HomePageView, MyProjectLoginView, RegisterUserView, MyProjectLogout



urlpatterns = [
    path('', HomePageView.as_view(), name='home'),
    path('logout/', MyProjectLogout.as_view(), name='logout_page'),
    path('login/', MyProjectLoginView.as_view(), name='login_page'),
    path('users/', UsersListView.as_view(), name='users'),
    path('users/create/', RegisterUserView.as_view(), name='register_page'),
]