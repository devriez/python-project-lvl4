from django.db import models
from django.urls import reverse


class Label(models.Model):
    name = models.CharField(max_length=150, verbose_name='Имя')
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('labels-list')
