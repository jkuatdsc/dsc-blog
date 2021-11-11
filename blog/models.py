from django.db import models
from django.utils import timezone
from PIL import Image


# Create your models here.

class Blog(models.Model):
    name = models.CharField(max_length=100)
    content = models.TextField(null=True)
    date_added = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return f"{self.name} - {self.date_added.date()}"


class News(models.Model):
    title = models.CharField(max_length=200, default='')
    content = models.TextField(default='')
    date_added = models.DateTimeField(default=timezone.now)


class Comment(models.Model):
    blog = models.ForeignKey(Blog, on_delete=models.CASCADE, null=True, blank=True)
    content = models.TextField(default='', blank=True, null=True)
    date_added = models.DateTimeField(default=timezone.now)
