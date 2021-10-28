from django.db import models
from django.utils import timezone


# Create your models here.

class Blog(models.Model):
    name = models.CharField(max_length=100, null=True)
    content = models.TextField(null=True, blank=False)
    date_added = models.DateTimeField(auto_now=True)


    def __str__(self): #double underscore
        return f"{self.name} : {self.date_added} "

    