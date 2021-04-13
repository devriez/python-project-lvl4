from django.shortcuts import render
from django.views.generic.list import ListView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from django.contrib.messages.views import SuccessMessageMixin

from statuses.models import Status
from statuses.forms import RegisterStatusesForm
from django.contrib.auth.mixins import LoginRequiredMixin
# Create your views here.

class StatusesListView(LoginRequiredMixin, ListView):
    model = Status
    template_name = 'statuses/statuses_list.html'
    context_object_name = 'statuses_list'
    login_url = reverse_lazy('login_page')
    redirect_field_name = 'redirect_to'

class CreateStatusView(LoginRequiredMixin, SuccessMessageMixin, CreateView):
    model = Status
    template_name = 'statuses/statuses_create.html'
    form_class = RegisterStatusesForm
    success_url = reverse_lazy('statuses')
    success_message = "Статус успешно создан"
    login_url = reverse_lazy('login_page')
    redirect_field_name = 'redirect_to'


class UpdateStatusView(LoginRequiredMixin, UpdateView):
    model = Status
    template_name = 'statuses/status_update_form.html'
    form_class = RegisterStatusesForm
    success_url = reverse_lazy('statuses')
    login_url = reverse_lazy('login_page')
    redirect_field_name = 'redirect_to'

class DeleteStatusView(LoginRequiredMixin, DeleteView):
    model = Status
    success_url = reverse_lazy('statuses')
    template_name = 'statuses/delete_status.html'
    login_url = reverse_lazy('login_page')
    redirect_field_name = 'redirect_to'