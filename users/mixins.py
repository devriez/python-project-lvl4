from django.urls import reverse_lazy
from django.shortcuts import redirect
from django.contrib import messages


class SelfEditPermissionMixin():

    def get(self, request, *args, **kwargs):
        self.permission_denied_message = 'У вас нет прав для изменения другого пользователя.'  # noqa: E501
        self.permission_denied_url = reverse_lazy('users-list')
        self.object = self.get_object()

        if self.object == self.request.user:
            return super().get(request, *args, **kwargs)
        else:
            messages.error(self.request, self.permission_denied_message)
            return redirect(self.permission_denied_url)
