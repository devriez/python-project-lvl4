from django.views.generic.edit import CreateView, DeleteView, UpdateView
from .models import Task
from django.urls import reverse_lazy
from django.contrib.messages.views import SuccessMessageMixin
from task_manager.mixins import AuthRequiredMixin
from tasks.mixins import OwnTaskDeletePermissionMixin
from django.views.generic.detail import DetailView
from django_filters.views import FilterView
from .filters import TaskFilter


class TasksListView(AuthRequiredMixin, FilterView):
    model = Task
    filterset_class = TaskFilter


class TaskCreateView(AuthRequiredMixin, SuccessMessageMixin, CreateView):
    model = Task
    success_message = 'Задача успешно создана'
    success_url = reverse_lazy('tasks-list')
    fields = ['name', 'description', 'executor', 'status', 'labels']

    def form_valid(self, form):
        form.instance.creator = self.request.user
        return super().form_valid(form)


class TaskDelete(AuthRequiredMixin, OwnTaskDeletePermissionMixin, SuccessMessageMixin, DeleteView):  # noqa: E501
    model = Task
    success_url = reverse_lazy('tasks-list')
    success_message = 'Задача успешно удалена'


class TaskUpdate(AuthRequiredMixin, SuccessMessageMixin, UpdateView):
    model = Task
    fields = ['name', 'description', 'executor', 'status', 'labels']
    success_url = reverse_lazy('tasks-list')
    success_message = 'Задача успешно изменена'
    template_name = 'tasks/task_update.html'


class TaskDetail(AuthRequiredMixin, DetailView):
    model = Task
