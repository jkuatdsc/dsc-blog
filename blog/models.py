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
    image = models.ImageField(default='dp.jpeg', upload_to='profile_pics/')

    def save(self, *args, **kwargs):
        img = Image.open(self.image.path)
        if img.height > 1000 or img.width > 1500:
            output_size = ((500, 500))
            img.thumbnail(output_size)
            img.save(self.image.path)
        super().save(*args, **kwargs)
