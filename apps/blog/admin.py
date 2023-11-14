from django.contrib import admin, messages
from mptt.admin import TreeRelatedFieldListFilter, DraggableMPTTAdmin
from django.http import HttpResponseRedirect
from django.contrib.admin import DateFieldListFilter
from django.urls import reverse, reverse_lazy
from admin_actions.admin import ActionsModelAdmin
from .models import (
    Tag,
    GalleryCategory,
    PostCategory,
    Gallery,
    Post,
    News,
)


@admin.register(Tag, GalleryCategory, PostCategory)
class TemplateAdmin(admin.ModelAdmin):
    list_display = 'title_ukr',
    list_display_links = 'title_ukr',
    search_fields = 'title_ukr',


@admin.register(Gallery,)
class GalleryAdmin(admin.ModelAdmin):
    list_display = 'pk', 'preview',
    list_display_links = 'pk',


@admin.register(Post)
class LessonThemeAdmin(ActionsModelAdmin):
    list_display = 'pk', 'title_ukr', 'small_image', 'display', 'created_at'
    list_display_links = 'title_ukr',
    filter_fields = 'display',
    search_fields = 'title_ukr',
    list_filter = (
        ('created_at', DateFieldListFilter),
    )
    actions_row = actions_detail = 'display_post', 'hide_post',
    filter_horizontal = (
        'related_gallery',
        'related_posts',
        'related_tags',
        'related_categories',
    )
    def display_post(self, request, pk):
        post = Post.objects.get(pk=pk)
        if post.display:
            messages.error(
                request, 'Публикация уже отображается')
            return HttpResponseRedirect(reverse_lazy('admin:blog_post_changelist'), request)
        else:
            messages.success(
                request, 'Публикация опубликована')
            post.display = True
            post.save()
            return HttpResponseRedirect(reverse_lazy('admin:blog_post_changelist'), request)

    def hide_post(self, request, pk):
        post = Post.objects.get(pk=pk)
        if not post.display:
            messages.error(
                request, 'Публикация уже спрятана')
            return HttpResponseRedirect(reverse_lazy('admin:blog_post_changelist'), request)
        else:
            messages.success(
                request, 'Публикация спрятана')
            post.display = False
            post.save()
            return HttpResponseRedirect(reverse_lazy('admin:blog_post_changelist'), request)

    display_post.short_description = 'Опубликовать'
    display_post.url_path = 'publish-post'
    hide_post.short_description = 'Спрятать'
    hide_post.url_path = 'hide-post'


@admin.register(News)
class NewsAdmin(ActionsModelAdmin):
    list_display = 'pk', 'title_ukr', 'small_image', 'display', 'created_at'
    list_display_links = 'title_ukr',
    filter_fields = 'display',
    search_fields = 'title_ukr',
    list_filter = (
        ('created_at', DateFieldListFilter),
    )
    actions_row = actions_detail = 'display_news', 'hide_news',
    filter_horizontal = (
        'related_tags',
    )

    def display_news(self, request, pk):
        news = News.objects.get(pk=pk)
        if news.display:
            messages.error(
                request, 'Публикация уже отображается')
            return HttpResponseRedirect(reverse_lazy('admin:blog_post_changelist'), request)
        else:
            messages.success(
                request, 'Публикация опубликована')
            news.display = True
            news.save()
            return HttpResponseRedirect(reverse_lazy('admin:blog_post_changelist'), request)

    def hide_news(self, request, pk):
        news = News.objects.get(pk=pk)
        if not news.display:
            messages.error(
                request, 'Публикация уже спрятана')
            return HttpResponseRedirect(reverse_lazy('admin:blog_post_changelist'), request)
        else:
            messages.success(
                request, 'Публикация спрятана')
            news.display = False
            news.save()
            return HttpResponseRedirect(reverse_lazy('admin:blog_post_changelist'), request)

    display_news.short_description = 'Опубликовать'
    display_news.url_path = 'publish-post'
    hide_news.short_description = 'Спрятать'
    hide_news.url_path = 'hide-post'
