from django.urls import path
from . import views
from rest_framework.urlpatterns import format_suffix_patterns


urlpatterns = [
    path('post/', views.PostList.as_view()),
    path('post/<int:pk>/', views.PostDetail.as_view()),
]

urlpatterns = format_suffix_patterns(urlpatterns)

# urlpatterns = [
#     path('', views.post_list_or_create, name='post_list'),
#     path('post/<int:pk>/', views.post_detail, name='post_detail'),
#     path('post/new/', views.post_list_or_create, name='post_new'),
#     path('post/<int:pk>/edit/', views.post_detail, name='post_edit'),
#     path('post/<int:pk>/delete/', views.post_detail, name='post_delete'),
# ]