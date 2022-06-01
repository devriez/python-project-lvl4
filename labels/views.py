from django.views.generic.list import ListView
from django.views.generic.edit import CreateView, DeleteView, UpdateView
from labels.models import Label
from django.urls import reverse_lazy
from django.contrib.messages.views import SuccessMessageMixin
from task_manager.mixins import AuthRequiredMixin
from django.contrib import messages
from django.shortcuts import redirect


class LabelsListView(AuthRequiredMixin, ListView):
    login_url = reverse_lazy('user-login')
    model = Label


class LabelCreateView(AuthRequiredMixin, SuccessMessageMixin, CreateView):
    model = Label
    fields = '__all__'
    success_message = 'Метка успешно создана'


class LabelDelete(AuthRequiredMixin, SuccessMessageMixin, DeleteView):
    model = Label
    success_url = reverse_lazy('labels-list')
    success_message = 'Метка успешно удалена'

    def post(self, request, *args, **kwargs):
        if self.get_object().task_set.all():
            messages.error(
                self.request,
                'Невозможно удалить метку, потому что она используется'
            )
            return redirect('labels-list')

        return super().post(request, *args, **kwargs)


class LabelUpdate(AuthRequiredMixin, SuccessMessageMixin, UpdateView):
    model = Label
    fields = '__all__'
    success_message = 'Метка успешно изменена'
    template_name = 'labels/label_update.html'
    success_url = reverse_lazy('labels-list')
