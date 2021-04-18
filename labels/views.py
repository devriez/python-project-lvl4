from django.shortcuts import render
from django.views.generic.list import ListView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from django.contrib.messages.views import SuccessMessageMixin
from django.contrib.auth.mixins import LoginRequiredMixin

from labels.models import Label
from labels.forms import RegisterLabelForm


class LabelsListView(LoginRequiredMixin, ListView):
    model = Label
    template_name = 'labels/labels_list.html'
    context_object_name = 'labels_list'
    login_url = reverse_lazy('login_page')
    redirect_field_name = 'redirect_to'

class CreateLabelView(LoginRequiredMixin, SuccessMessageMixin, CreateView):
    model = Label
    template_name = 'labels/label_create.html'
    form_class = RegisterLabelForm
    success_url = reverse_lazy('labels')
    success_message = "Метка успешно создан"
    login_url = reverse_lazy('login_page')
    redirect_field_name = 'redirect_to'


class UpdateLabelView(LoginRequiredMixin, UpdateView):
    model = Label
    template_name = 'labels/label_update_form.html'
    form_class = RegisterLabelForm
    success_url = reverse_lazy('labels')
    login_url = reverse_lazy('login_page')
    redirect_field_name = 'redirect_to'

class DeleteLabelView(LoginRequiredMixin, DeleteView):
    model = Label
    success_url = reverse_lazy('labels')
    template_name = 'labels/delete_label.html'
    login_url = reverse_lazy('login_page')
    redirect_field_name = 'redirect_to'