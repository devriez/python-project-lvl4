from django.db import models

class Label(models.Model):
    name = models.CharField(max_length=30)
    created_at = models.DateTimeField(auto_now_add=True)
    
    class Meta(object):
        verbose_name = 'label'
        verbose_name_plural = 'labels'

    def __str__(self):
        return self.name
