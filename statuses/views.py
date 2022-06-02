from django.views.generic.list import ListView
from django.views.generic.edit import CreateView, DeleteView, UpdateView
from statuses.models import Status
from statuses.forms import StatusForm
from django.urls import reverse_lazy
from django.contrib.messages.views import SuccessMessageMixin
from task_manager.mixins import AuthRequiredMixin
from django.contrib import messages
from django.shortcuts import redirect


class StatusListView(AuthRequiredMixin, ListView):
    login_url = reverse_lazy('user-login')
    model = Status


class StatusCreateView(AuthRequiredMixin, SuccessMessageMixin, CreateView):
    model = Status
    form_class = StatusForm
    success_url = reverse_lazy('statuses-list')
    success_message = 'Статус успешно создан'


class StatusDelete(AuthRequiredMixin, SuccessMessageMixin, DeleteView):
    model = Status
    success_url = reverse_lazy('statuses-list')
    success_message = 'Статус успешно удалён'

    def post(self, request, *args, **kwargs):
        if self.get_object().task_set.all():
            messages.error(
                self.request,
                'Невозможно удалить статус, потому что он используется'
            )
            return redirect('statuses-list')

        return super().post(request, *args, **kwargs)


class StatusUpdate(AuthRequiredMixin, SuccessMessageMixin, UpdateView):
    model = Status
    form_class = StatusForm
    success_message = 'Статус успешно изменён'
    template_name = 'statuses/status_update.html'
    success_url = reverse_lazy('statuses-list')
