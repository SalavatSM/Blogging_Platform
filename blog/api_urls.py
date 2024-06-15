from django.urls import path
from .views import BlogListCreate, BlogDetail, PostListCreate, PostDetail

urlpatterns = [
    path('blogs/', BlogListCreate.as_view(), name='blog-list-create'),
    path('blogs/<int:pk>/', BlogDetail.as_view(), name='blog-detail'),
    path('posts/', PostListCreate.as_view(), name='post-list-create'),
    path('posts/<int:pk>/', PostDetail.as_view(), name='post-detail'),
]

