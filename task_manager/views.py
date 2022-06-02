from django.contrib.auth.views import LoginView, LogoutView
from django.contrib.messages.views import SuccessMessageMixin
from django.contrib import messages
from django.urls import reverse_lazy


class UserLogin(SuccessMessageMixin, LoginView):
    template_name = 'task_manager/login.html'
    success_message = 'Вы залогинены'
    success_url = reverse_lazy('start-page')


class UserLogout(LogoutView):
    def dispatch(self, request, *args, **kwargs):
        messages.info(request, 'Вы разлогинены')
        return super().dispatch(request, *args, **kwargs)
