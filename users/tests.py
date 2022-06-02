from django.test import TestCase
from django.contrib.auth import get_user_model
from django.urls import reverse


class UserTest(TestCase):

    fixtures = ['users.json']

    def assertUser(self, user, data):
        self.assertEqual(user.first_name, data['first_name'])
        self.assertEqual(user.last_name, data['last_name'])
        self.assertEqual(user.username, data['username'])

    def test_get_users(self):
        """Tests GET /users/"""
        response = self.client.get(reverse("users-list"))
        self.assertEqual(response.status_code, 200)

    def test_get_users_create(self):
        """Tests GET /users/create/"""
        response = self.client.get(reverse('user-create'))
        self.assertEqual(response.status_code, 200)

    def test_post_users_create(self):
        """Tests POST /users/create/"""
        user_to_create = {
            'first_name': 'John',
            'last_name': 'Smith',
            'username': 'jsmith',
            'password1': 'asgkjKJKJ98',
            'password2': 'asgkjKJKJ98',
        }

        response = self.client.post(reverse('user-create'), user_to_create)
        self.assertRedirects(response, reverse('user-login'))
        user = get_user_model().objects.get(
            username=user_to_create['username']
        )
        self.assertUser(user, user_to_create)

    def test_get_users_update(self):
        """Tests GET /users/<int:pk>/update/"""
        user = get_user_model().objects.first()
        password = 'test_password'
        response = self.client.login(username=user.username, password=password)
        self.assertTrue(response)

        response = self.client.get(reverse('user-update', args=[user.pk]))
        self.assertEqual(response.status_code, 200)

    def test_post_users_update(self):
        """Tests POST /users/<int:pk>/update/"""
        user = get_user_model().objects.first()
        password = 'test_password'
        response = self.client.login(username=user.username, password=password)
        self.assertTrue(response)

        old_username = user.username
        new_username = old_username[::-1]

        user_to_update = {
            'first_name': 'John',
            'last_name': 'Smith',
            'username': new_username,
            'password1': 'asgkjKJKJ98',
            'password2': 'asgkjKJKJ98',
        }

        response = self.client.post(
            reverse('user-update', args=[user.pk]),
            user_to_update
        )
        self.assertRedirects(response, reverse('users-list'))
        user.refresh_from_db()

        self.assertEqual(user.username, new_username)

    def test_get_user_delete(self):
        """Tests GET /users/<int:pk>/delete/"""
        user = get_user_model().objects.first()
        password = 'test_password'
        response = self.client.login(username=user.username, password=password)
        self.assertTrue(response)

        response = self.client.get(reverse('user-delete', args=[user.id]))
        self.assertEqual(response.status_code, 200)

    def test_post_user_delete(self):
        """Tests POST /users/<int:pk>/delete/"""
        user = get_user_model().objects.first()
        password = 'test_password'
        response = self.client.login(username=user.username, password=password)
        self.assertTrue(response)

        response = self.client.post(reverse('user-delete', args=[user.pk]))
        self.assertRedirects(response, reverse('users-list'))
        self.assertEqual(get_user_model().objects.count(), 0)

    def test_get_user_login(self):
        """Tests GET /login"""
        response = self.client.get(reverse('user-login'))
        self.assertEqual(response.status_code, 200)

    def test_post_login(self):
        """Tests POST /login/"""
        user = get_user_model().objects.first()
        password = 'test_password'
        response = self.client.post(reverse('user-login'), {
            'username': user.username,
            'password': password,
        })
        self.assertRedirects(response, reverse('start-page'))
