from django.shortcuts import render
from django.views.generic.list import ListView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from django.contrib.messages.views import SuccessMessageMixin

from tasks.models import Task
from tasks.forms import RegisterTaskForm
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin

class TasksListView(LoginRequiredMixin, ListView):
    model = Task
    template_name = 'tasks/tasks_list.html'
    context_object_name = 'tasks_list'
    login_url = reverse_lazy('login_page')
    redirect_field_name = 'redirect_to'

class CreateTaskView(LoginRequiredMixin, SuccessMessageMixin, CreateView):
    model = Task
    template_name = 'tasks/task_create.html'
    form_class = RegisterTaskForm
    success_url = reverse_lazy('tasks')
    success_message = "Статус успешно создан"
    login_url = reverse_lazy('login_page')
    redirect_field_name = 'redirect_to'

    def form_valid(self, form):
        form.instance.creator = self.request.user
        return super().form_valid(form)


class UpdateTaskView(LoginRequiredMixin, UpdateView):
    model = Task
    template_name = 'tasks/task_update_form.html'
    form_class = RegisterTaskForm
    success_url = reverse_lazy('tasks')
    login_url = reverse_lazy('login_page')
    redirect_field_name = 'redirect_to'

class DeleteTaskView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Task
    success_url = reverse_lazy('tasks')
    template_name = 'tasks/delete_task.html'
    login_url = reverse_lazy('login_page')
    redirect_field_name = 'redirect_to'

    def test_func(self):
        task = self.get_object()
        return self.request.user == task.creator