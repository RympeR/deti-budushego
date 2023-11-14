from django.urls import path
from .views import (PostList, PostDetail, GalleryList, PostListFiltered, NewsDetail, NewsList, NewsListFiltered)

app_name = 'blog_section'

urlpatterns = [
    path('posts/', PostList.as_view(), name='post_list'),
    path('posts/<slug:slug>', PostDetail.as_view(), name='post_detail'),
    path('posts-filtered/<slug:slug>', PostListFiltered.as_view(), name='post_detail_filtered'),
    path('info/', NewsList.as_view(), name='news_list'),
    path('info/<slug:slug>', NewsDetail.as_view(), name='news_detail'),
    path('info-filtered/<slug:slug>', NewsListFiltered.as_view(), name='news_detail_filtered'),
    path('gallery/', GalleryList.as_view(), name='gallery'),
]
