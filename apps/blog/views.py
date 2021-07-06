from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from apps.lessons.models import Event
from .models import (
    Tag,
    GalleryCategory,
    PostCategory,
    Gallery,
    Post,
)
from apps.users.models import MenuCategory


class PostList(ListView):
    model = Post
    context_object_name = 'posts'
    template_name = 'blog-grid.html'
    paginate_by = 9

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['menu'] = MenuCategory.objects.filter(display=True)
        context['footer_events'] = Event.objects.all().order_by('-date_start')[:2]
        return context

class PostDetail(DetailView):
    model = Post
    template_name = 'blog-single.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['categories'] = PostCategory.objects.all()
        context['tags'] = Tag.objects.all()
        context['menu'] = MenuCategory.objects.filter(display=True)
        context['footer_events'] = Event.objects.all().order_by('-date_start')[:2]
        return context


class GalleryList(ListView):
    model = Gallery
    context_object_name = 'gallery'
    template_name = 'gallery-3.html'
    paginate_by = 9

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['categories'] = GalleryCategory.objects.all()
        context['tags'] = Tag.objects.all()
        context['menu'] = MenuCategory.objects.filter(display=True)
        context['footer_events'] = Event.objects.all().order_by('-date_start')[:2]
        return context
