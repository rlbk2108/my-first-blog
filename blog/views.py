from django.contrib.auth.models import User
from djangogirls.blog.permissions import IsOwnerOrReadOnly
from rest_framework import generics, permissions, viewsets, renderers
from rest_framework.decorators import action
from rest_framework.response import Response


from .models import Post
from .serializers import PostSerializer, UserSerializer


class PostViewSet(viewsets.ModelViewSet):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly,
                          IsOwnerOrReadOnly]

    @action(detail=True, renderer_classes=[renderers.StaticHTMLRenderer])
    def highlight(self, request, *args, **kwargs):
        post = self.get_object()
        return Response(post.highlighted)

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)


class UserViewSet(viewsets.ReadOnlyModelViewSet):
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