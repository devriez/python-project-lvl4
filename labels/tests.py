from django.test import TestCase
from django.contrib.auth import get_user_model
from django.urls import reverse
from .models import Label


class LabelTest(TestCase):

    fixtures = ['users.json', 'labels.json']

    def setUp(self):
        user = get_user_model().objects.first()
        password = 'test_password'
        response = self.client.login(username=user.username, password=password)
        self.assertTrue(response)

    def test_get_labels_list(self):
        """Tests GET /labels/"""
        response = self.client.get(reverse('labels-list'))
        self.assertEqual(response.status_code, 200)

    def test_get_label_create(self):
        """Tests GET /labels/create/"""
        response = self.client.get(reverse('label-create'))
        self.assertEqual(response.status_code, 200)

    def test_post_label_create(self):
        """Tests POST /labels/create/"""
        name = 'new label'
        response = self.client.post(reverse('label-create'), {'name': name})
        self.assertRedirects(response, reverse('labels-list'))
        label = Label.objects.last()
        self.assertEqual(label.name, name)

    def test_get_label_update(self):
        """Tests GET /labels/<id>/update/"""
        label = Label.objects.first()
        response = self.client.get(reverse('label-update', args=[label.id]))
        self.assertEqual(response.status_code, 200)

    def test_post_label_update(self):
        """Tests POST /labels/<id>/update/"""
        label = Label.objects.first()
        name = 'new name'
        response = self.client.post(reverse('label-update', args=[label.id]), {
            'name': name
            }
            )
        self.assertRedirects(response, reverse('labels-list'))
        label.refresh_from_db()
        self.assertEqual(label.name, name)

    def test_get_label_delete(self):
        """Tests GET /labels/<id>/delete/"""
        label = Label.objects.first()
        response = self.client.get(reverse('label-delete', args=[label.id]))
        self.assertEqual(response.status_code, 200)

    def test_post_label_delete(self):
        """Tests POST /labels/<id>/delete/"""
        label = Label.objects.first()
        response = self.client.post(reverse('label-delete', args=[label.id]))
        self.assertRedirects(response, reverse('labels-list'))
        self.assertEqual(Label.objects.count(), 0)
