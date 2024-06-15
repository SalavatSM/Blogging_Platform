from django.contrib import admin
from django.urls import path, include
from django.shortcuts import redirect

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include('blog.api_urls')),  # Отдельный файл для API маршрутов
    path('blogs/', include('blog.urls')),    # Обычные представления
    path('', lambda request: redirect('blog-list')),
    path('posts/', lambda request: redirect('post-list')),
]


