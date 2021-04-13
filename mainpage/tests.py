from django.test import TestCase

from django.contrib.auth.models import User

from .views import RegisterUserView, DeleteUserView, UpdateUserView
from mainpage.forms import RegisterUserForm
from django.urls import reverse

# Create your tests here.
class UserTestCase(TestCase):
    def setUp(self):
        self.client.post('/users/create/', {'first_name': 'test',
                                        'last_name': 'test',
                                        'username': 'test',
                                        'password1': 'BL1POREEKO3',
                                        'password2': 'BL1POREEKO3'})

    def test_user_create(self):
        user = User.objects.get(pk=1)
        self.assertEqual(user.username, 'test')
    
    def test_user_login(self):
        self.client.post('/login/', {'username': 'test', 'password': 'BL1POREEKO3'})
        user = User.objects.get(pk=1)
        self.assertEqual(user.id, int(self.client.session['_auth_user_id']))

    def test_user_delete(self):
        self.client.post('/login/', {'username': 'test', 'password': 'BL1POREEKO3'})
        url = reverse('delete_user', kwargs={'pk': 1})
        self.client.delete(url)
        self.assertEqual(User.objects.count(), 0)


