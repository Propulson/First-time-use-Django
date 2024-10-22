from django.db import models
from django.contrib.auth.models import User


# Create your models here.

class Topic(models.Model):
    """Theme which user exploration"""
    text = models.CharField(max_length=200)
    date_added = models.DateTimeField(auto_now_add=True)
    owner = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        """return string models"""
        return self.text


class Entry(models.Model):
    """Information, which user learned"""
    topic = models.ForeignKey(Topic, on_delete=models.CASCADE)
    text = models.TextField()
    date_added = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name_plural = 'entries'

    def __str__(self):
        """return string"""
        if self.text[:50] >= '50':
            return f'{self.text[:50]}...'
