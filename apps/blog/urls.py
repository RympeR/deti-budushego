from django.urls import path
from .views import (
    PostList,
    PostDetail,
    GalleryList,
    PostListFiltered,
)

app_name = 'blog_section'

urlpatterns = [
    path('posts/', PostList.as_view(), name='post_list'),
    path('posts/<slug:slug>', PostDetail.as_view(), name='post_detail'),
    path('posts-filtered/<slug:slug>', PostListFiltered.as_view(), name='post_detail_filtered'),
    path('gallery/', GalleryList.as_view(), name='gallery'),
]
