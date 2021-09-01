from django.views.generic.list import ListView
from django.views.generic.base import TemplateView
from django.views.generic.detail import DetailView
from .models import (
    Faq,
    LessonCategory,
    EventCategory,
    Event,
    Lesson,
)
from apps.users.models import (
    MenuCategory,
    User,
    Schedule,
    ParentComment,
    MainCounters,
    AboutCounters,
    DropDownPoint,
)
from apps.blog.models import Gallery, Post, Tag
from core.utils.mixins import (
    FooterContentMixin,
)


class LessonList(FooterContentMixin, ListView):
    model = Lesson
    context_object_name = 'lessons'
    template_name = 'classes.html'
    paginate_by = 9
    base_context = {'categories': LessonCategory.objects.all()}
    
    def get_queryset(self):
        return Lesson.objects.filter(display=True)

class LessonListFiltered(FooterContentMixin, ListView):
    model = Lesson
    context_object_name = 'lessons'
    template_name = 'classes.html'
    paginate_by = 9

    def get_queryset(self):
        tag = Tag.objects.get(slug=self.kwargs['slug'])
        return Lesson.objects.filter(tags__in=[tag])


class LessonDetail(FooterContentMixin, DetailView):
    model = Lesson
    template_name = 'class-single.html'


class EventsList(FooterContentMixin, ListView):
    model = Event
    context_object_name = 'events'
    template_name = 'events.html'
    paginate_by = 9
    base_context = {'categories': EventCategory.objects.all()}


class EventsListFiltered(FooterContentMixin, ListView):
    model = Event
    context_object_name = 'events'
    template_name = 'events.html'
    paginate_by = 9

    def get_queryset(self):
        tag = Tag.objects.get(slug=self.kwargs['slug'])
        return Event.objects.filter(tags__in=[tag])


class EventDetail(FooterContentMixin, DetailView):
    model = Event
    template_name = 'events-single.html'


class Index(FooterContentMixin, TemplateView):
    template_name = 'index.html'
    base_context = {
        'classes': Lesson.objects.filter(most_popular=True, display=True),
        'gallery': Gallery.objects.filter(most_popular=True),
        'teachers': User.objects.filter(most_popular=True),
        'events': Event.objects.filter(most_popular=True),
        'drop_down': DropDownPoint.objects.filter(main_page=True),
        'schedule': Schedule.objects.all(),
        'comments': ParentComment.objects.all(),
        'counters': MainCounters.objects.all(),
    }


class About(FooterContentMixin, TemplateView):
    template_name = 'about.html'
    base_context = {
        'teachers': User.objects.filter(most_popular=True),
        'posts': Post.objects.filter(most_popular=True),
        'teachers': User.objects.filter(most_popular=True),
        'drop_down': DropDownPoint.objects.filter(main_page=False),
        'counters': AboutCounters.objects.all(),
    }


class Schedule(FooterContentMixin, TemplateView):
    template_name = 'class-schedule.html'
    base_context = {'schedule': Schedule.objects.all()}


class Contact(FooterContentMixin, TemplateView):
    template_name = 'contact.html'


class ComingSoon(FooterContentMixin, TemplateView):
    template_name = 'coming-soon.html'


class FAQ(FooterContentMixin, TemplateView):
    template_name = 'faqs.html'
    base_context = {
        'left': Faq.objects.filter(right=False),
        'right': Faq.objects.filter(right=True),
    }


class Login(FooterContentMixin, TemplateView):
    template_name = 'login.html'


class Registration(FooterContentMixin, TemplateView):
    template_name = 'registration.html'
