from django.urls import reverse_lazy
from django.shortcuts import redirect
from django.contrib import messages


class OwnTaskDeletePermissionMixin():

    def get(self, request, *args, **kwargs):
        self.permission_denied_message = 'Задачу может удалить только её автор'
        self.permission_denied_url = reverse_lazy('tasks-list')
        self.object = self.get_object()

        if self.object.creator == self.request.user:
            return super().get(request, *args, **kwargs)
        else:
            messages.error(self.request, self.permission_denied_message)
            return redirect(self.permission_denied_url)
