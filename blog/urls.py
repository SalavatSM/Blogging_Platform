from django.urls import path
from .views import blog_list, blog_detail, post_list, post_detail

urlpatterns = [
    path('', blog_list, name='blog-list'),
    path('<int:pk>/', blog_detail, name='blog-detail'),
    path('posts/', post_list, name='post-list'),
    path('posts/<int:pk>/', post_detail, name='post-detail'),
]



