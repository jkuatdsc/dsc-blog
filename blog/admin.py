from django.contrib import admin
from .models import Blog, News, Comment

# Register your models here.
admin.site.register(Blog)
admin.site.register(News)
admin.site.register(Comment)
