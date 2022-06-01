from django.test import TestCase
from django.contrib.auth import get_user_model
from django.urls import reverse
from .models import Task


class TaskTest(TestCase):
    fixtures = ['users.json', 'statuses.json', 'tasks.json', 'labels.json']

    def setUp(self):
        user = get_user_model().objects.first()
        password = 'test_password'
        self.client.login(
            username=user.username,
            password=password,
        )

    def assertTask(self, task, data):
        self.assertEqual(task.name, data['name'])
        self.assertEqual(task.description, data['description'])
        self.assertEqual(task.status.id, data['status'])
        self.assertEqual(task.executor.id, data['executor'])

    def test_get_tasks(self):
        """Tests GET /tasks/"""
        response = self.client.get(reverse('tasks-list'))
        self.assertEqual(response.status_code, 200)

    def test_get_task_create(self):
        """Tests GET /tasks/create"""
        response = self.client.get(reverse('task-create'))
        self.assertEqual(response.status_code, 200)

    def test_post_task_create(self):
        """Tests POST /tasks/create"""
        task_data = {
            'name': 'new_status',
            'description': 'new_description',
            'status': 1,
            'executor': 12,
        }
        response = self.client.post(reverse('task-create'), task_data)
        self.assertRedirects(response, reverse('tasks-list'))
        created_task = Task.objects.last()
        self.assertTask(created_task, task_data)

    def test_get_task_detail(self):
        """Tests GET /tasks/<int:pk>"""
        task = Task.objects.first()
        response = self.client.get(reverse('task-detail', args=[task.id]))
        self.assertEqual(response.status_code, 200)

    def test_get_task_edit(self):
        """Tests GET /tasks/<int:pk>/edite"""
        task = Task.objects.first()
        response = self.client.get(reverse('task-update', args=[task.id]))
        self.assertEqual(response.status_code, 200)

    def test_post_task_edit(self):
        """Tests POST /tasks/<int:pk>/edite"""
        task = Task.objects.first()
        task_edit_data = {
            'name': 'new_status_edit',
            'description': 'new_description_edit',
            'status': 1,
            'executor': 12,
        }
        response = self.client.post(
            reverse('task-update', args=[task.id]),
            task_edit_data
            )
        self.assertRedirects(response, reverse('tasks-list'))
        task.refresh_from_db()
        self.assertTask(task, task_edit_data)

    def test_get_task_delete(self):
        """Tests GET /tasks/<int:pk>/delete"""
        task = Task.objects.first()
        response = self.client.get(
            reverse('task-delete', args=[task.id])
            )
        self.assertEqual(response.status_code, 200)

    def test_post_task_delete(self):
        """Tests POST /tasks/<int:pk>/delete"""
        task = Task.objects.first()
        response = self.client.post(reverse(
            'task-delete',
            args=[task.id]
            ))
        self.assertRedirects(response, reverse('tasks-list'))
        self.assertEqual(Task.objects.count(), 0)
