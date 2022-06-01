from django.contrib.auth.views import LoginView, LogoutView
from django.urls import reverse_lazy


class UserLogin(LoginView):
    template_name = 'task_manager/login.html'
    success_message = 'Вы залогинены'
    success_url = reverse_lazy('start-page')


class UserLogout(LogoutView):
    success_message = 'Вы разлогинены'
    success_url = reverse_lazy('users-list')
