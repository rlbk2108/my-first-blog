from django.contrib.auth.models import User
from djangogirls.blog.permissions import IsOwnerOrReadOnly
from rest_framework import generics, permissions

from .models import Post
from .serializers import PostSerializer, UserSerializer


class PostList(generics.ListCreateAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

    def perform_create(self, serializer):
        serializer.save(author=self.request.user)


class PostDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly,
                          IsOwnerOrReadOnly]


class UserList(generics.ListAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer


class UserDetail(generics.RetrieveAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer

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
