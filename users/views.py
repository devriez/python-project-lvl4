from django.views.generic.list import ListView
from django.views.generic.edit import CreateView, DeleteView, UpdateView
from django.urls import reverse_lazy
from users.forms import UserForm
from django.contrib.auth import get_user_model
from .mixins import SelfEditPermissionMixin
from django.contrib.messages.views import SuccessMessageMixin
from django.contrib import messages
from django.shortcuts import redirect
from task_manager.mixins import AuthRequiredMixin


class UserListView(ListView):
    model = get_user_model()
    template_name = 'users/user_list.html'


class UserCreate(SuccessMessageMixin, CreateView):
    template_name = 'users/user_create.html'
    model = get_user_model()
    form_class = UserForm
    success_url = reverse_lazy('user-login')
    success_message = 'Пользователь успешно зарегистрирован'


class UserUpdate(AuthRequiredMixin, SelfEditPermissionMixin, SuccessMessageMixin, UpdateView):  # noqa: E501
    template_name = 'users/user_update.html'
    model = get_user_model()
    form_class = UserForm
    success_url = reverse_lazy('users-list')
    success_message = 'Пользователь успешно изменен'


class UserDelete(SelfEditPermissionMixin, SuccessMessageMixin, DeleteView):
    template_name = 'users/user_delete.html'
    model = get_user_model()
    success_url = reverse_lazy('users-list')
    success_message = 'Пользователь успешно удален'

    def post(self, request, *args, **kwargs):
        if self.get_object().creator.all() or self.get_object().executor.all():
            messages.error(
                self.request,
                'Невозможно удалить пользователя, потому что он используется'
            )
            return redirect('statuses-list')

        return super().post(request, *args, **kwargs)
