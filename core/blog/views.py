from django.shortcuts import render
from django.views.generic import ListView

from blog.models import Post


class HomeView(ListView):
    model = Post
    context_object_name = 'posts'
