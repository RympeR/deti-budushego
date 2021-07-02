from django.urls import path
from .views import (
    PostList,
    PostDetail,
    GalleryList,
)

app_name = 'blog_section'

urlpatterns = [
    path('posts/', PostList.as_view(), name='post_list'),
    path('posts/<slug:slug>', PostDetail.as_view(), name='post_detail'),
    path('gallery/', GalleryList.as_view(), name='gallery'),
]
