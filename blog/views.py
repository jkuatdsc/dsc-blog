from django.shortcuts import render
from django.http import HttpResponse
from .models import Blog

def home(request):
    blog = Blog.objects.filter(name = "Mercy Irene")
    q = blog.query
    return HttpResponse(q)

# Create your views here.
