from django.http import Http404
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from .models import Post
from .serializers import PostSerializer
from rest_framework import generics


class PostList(generics.ListCreateAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer


class PostDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer

# class PostListView(ListView):
#     model = Post
#     context_object_name = 'posts'


# class PostDetailView(DetailView):
#     model = Post
#     context_object_name = 'post'


# class PostCreateView(CreateView):
#     model = Post
#     form_class = CreateForm
#     success_url = reverse_lazy('post_list')
#     template_name = 'blog/post_new.html'


# class PostUpdateView(UpdateView):
#     model = Post
#     form_class = PostForm
#     success_url = reverse_lazy('post_list')
#     template_name = 'blog/post_edit.html'
#
#
# class PostDeleteView(DeleteView):
#     model = Post
#     success_url = reverse_lazy('post_list')
#     template_name = 'blog/post_delete.html'
