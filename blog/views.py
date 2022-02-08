from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse_lazy

from .models import Post
from django.utils import timezone
from .forms import PostForm, CreateForm
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.contrib.auth.views import LoginView


class PostListView(ListView):
    model = Post
    context_object_name = 'posts'


class PostDetailView(DetailView):
    model = Post
    context_object_name = 'post'


class PostCreateView(CreateView):
    model = Post
    form_class = CreateForm
    success_url = reverse_lazy('post_list')
    template_name = 'blog/post_new.html'


class PostUpdateView(UpdateView):
    model = Post
    fields = ['title, text']


class PostDeleteView(DeleteView):
    model = Post
    success_url = reverse_lazy('post_list')
    template_name = 'blog/post_delete.html'
