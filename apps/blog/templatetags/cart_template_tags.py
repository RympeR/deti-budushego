from apps.blog.models import *
from apps.lessons.models import *
from apps.users.models import *
from django import template



register = template.Library()

@register.filter
def post_categories(request):
    qs = PostCategory.objects.all()
    if qs.exists():
        return qs
    return 0

@register.filter
def gallery_categories(request):
    qs = GalleryCategory.objects.all()
    if qs.exists():
        return qs
    return 0

@register.filter
def lesson_categories(request):
    qs = LessonCategory.objects.all()
    if qs.exists():
        return qs
    return 0

@register.filter
def events_categories(request):
    qs = EventCategory.objects.all()
    if qs.exists():
        return qs
    return 0
