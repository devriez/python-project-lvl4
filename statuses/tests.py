from django.test import TestCase
from .models import Status
from django.contrib.auth import get_user_model
from django.urls import reverse


class StatusTest(TestCase):
    fixtures = ['users.json', 'statuses.json']

    def setUp(self):
        user = get_user_model().objects.first()
        password = 'test_password'
        self.client.login(username=user.username, password=password)

    def test_get_statuses(self):
        """Tests GET /statuses/"""
        response = self.client.get(reverse('statuses-list'))
        self.assertEqual(response.status_code, 200)

    def test_get_statuses_create(self):
        """Tests GET /statuses/create"""
        response = self.client.get(reverse('status-create'))
        self.assertEqual(response.status_code, 200)

    def test_post_statuses_create(self):
        """Tests POST /statuses/create"""
        name = 'status_create'
        response = self.client.post(reverse('status-create'), {'name': name})
        self.assertRedirects(response, reverse('statuses-list'))
        status = Status.objects.last()
        self.assertEqual(status.name, name)

    def test_get_status_update(self):
        """Tests GET /statuses/update"""
        status = Status.objects.first()
        response = self.client.get(reverse('status-update', args=[status.id]))
        self.assertEqual(response.status_code, 200)

    def test_post_status_udate(self):
        """Tests POST /statuses/update"""
        status = Status.objects.first()
        old_name = status.name
        new_name = old_name[::-1]
        response = self.client.post(reverse(
            'status-update',
            args=[status.id]),
            {'name': new_name}
            )
        status.refresh_from_db()
        self.assertRedirects(response, reverse('statuses-list'))
        self.assertEqual(status.name, new_name)

    def test_get_status_delete(self):
        """Tests GET /statuses/delete"""
        status = Status.objects.first()
        response = self.client.get(reverse('status-delete', args=[status.id]))
        self.assertEqual(response.status_code, 200)

    def test_post_status_update(self):
        """Tests POST /statuses/delete"""
        status = Status.objects.first()
        response = self.client.post(reverse('status-delete', args=[status.id]))
        self.assertRedirects(response, reverse('statuses-list'))
        self.assertEqual(Status.objects.count(), 0)
