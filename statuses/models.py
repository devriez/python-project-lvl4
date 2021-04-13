from django.db import models

class Status(models.Model):
    name = models.CharField(max_length=30)
    created_at = models.DateTimeField(auto_now_add=True)
    
    class Meta(object):
        verbose_name = 'status'
        verbose_name_plural = 'statuses'

    def __str__(self):
        return self.name
