from django.test import TestCase

from .models import Status

from django.urls import reverse


class UserTestCase(TestCase):
    def setUp(self):
        url = reverse('create_status')
        self.client.post(url, {'name': 'test'})

    def test_status_create(self):
        status = Status.objects.get(pk=1)
        self.assertEqual(status.name, 'test')

    def test_status_delete(self):
        url = reverse('delete_status', kwargs={'pk': 1})
        self.client.delete(url)
        self.assertEqual(Status.objects.count(), 0)

    def test_status_update(self):
        url = reverse('update_status', kwargs={'pk': 1})
        self.client.post(url, {'name': 'test2'})
        status = Status.objects.get(pk=1)
        self.assertEqual(status.name, 'test2')
