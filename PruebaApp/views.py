from __future__ import unicode_literals

from django.shortcuts import render

# Create your views here.

from .models import Post

def posts(request):
    posts = Post.objects.all()
    return render(request, 'posts.html', {'posts': posts})