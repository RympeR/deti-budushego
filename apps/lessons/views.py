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
    FooterContentMixin
)
from django.shortcuts import render
from django.template import RequestContext
from datetime import datetime, timedelta


def handler404(request, *args):
    return render(request, '404.html')


def handler500(request, *args):
    return render(request, '404.html')


class LessonList(ListView):
    model = Lesson
    context_object_name = 'lessons'
    template_name = 'classes.html'
    paginate_by = 9

    def get_queryset(self):
        return Lesson.objects.filter(display=True)

    def get_context_data(self, **kwargs: any) -> dict:
        context = super().get_context_data(**kwargs)
        context['title'] = 'Групи'
        footer_context = {
            'categories': LessonCategory.objects.all(),
            'menu': MenuCategory.objects.filter(display=True),
            'footer_events': Event.objects.all().order_by(
                '-date_start')[:2]
        }
        context = {**context, **footer_context}
        return context


class LessonListFiltered(ListView):
    model = Lesson
    context_object_name = 'lessons'
    template_name = 'classes.html'
    paginate_by = 9

    def get_queryset(self):
        tag = Tag.objects.get(slug=self.kwargs['slug'])
        return Lesson.objects.filter(tags__in=[tag], display=True)

    def get_context_data(self, **kwargs: any) -> dict:
        context = super().get_context_data(**kwargs)
        context['title'] = 'Групи'
        footer_context = {
            'menu': MenuCategory.objects.filter(display=True),
            'footer_events': Event.objects.all().order_by(
                '-date_start')[:2]
        }
        context = {**context, ** footer_context}
        return context


class LessonListFilteredByTag(ListView):
    model = Lesson
    context_object_name = 'lessons'
    template_name = 'classes.html'
    paginate_by = 9

    def get_queryset(self):
        if self.kwargs['slug'] == 'all':
            return Lesson.objects.all()
        lessonCategory = LessonCategory.objects.get(slug=self.kwargs['slug'])
        return Lesson.objects.filter(category__in=[lessonCategory], display=True)

    def get_context_data(self, **kwargs: any) -> dict:
        context = super().get_context_data(**kwargs)
        context['title'] = 'Групи'
        context['active_tag'] = self.kwargs['slug']
        footer_context = {
            'menu': MenuCategory.objects.filter(display=True),
            'footer_events': Event.objects.all().order_by(
                '-date_start')[:2]
        }
        context = {**context, **footer_context}
        return context


class LessonDetail(DetailView):
    model = Lesson
    template_name = 'class-single.html'

    def get_context_data(self, **kwargs: any) -> dict:
        context = super().get_context_data(**kwargs)
        context['title'] = context['object'].title_ukr
        footer_context = {
            'menu': MenuCategory.objects.filter(display=True),
            'footer_events': Event.objects.all().order_by('-date_start')[:2]
        }
        context = {**context, **footer_context}
        return context


def filter_date(date_obj):
    if date_obj.date_start > datetime.now().date():
        return date_obj.date_start - datetime.now().date()
    return date_obj.date_start - datetime.now().date() + timedelta(365)


class EventsList(ListView, FooterContentMixin):
    model = Event
    context_object_name = 'events'
    template_name = 'events.html'
    paginate_by = 9
    base_context = {'categories': EventCategory.objects.all()}

    def get_queryset(self):
        return sorted(Event.objects.all(), key=filter_date)

    def get_context_data(self, **kwargs: any) -> dict:
        context = super().get_context_data(**kwargs)
        context['title'] = 'Заходи'
        footer_context = {
            'menu': MenuCategory.objects.filter(display=True),
            'footer_events': Event.objects.all().order_by('-date_start')[:2]
        }
        base_context = {'categories': EventCategory.objects.all()}
        context = {**context, **base_context, **footer_context}
        return context


class EventsListFiltered(ListView):
    model = Event
    context_object_name = 'events'
    template_name = 'events.html'
    paginate_by = 9

    def get_queryset(self):
        tag = Tag.objects.get(slug=self.kwargs['slug'])
        return sorted(Event.objects.filter(tags__in=[tag]), key=filter_date)

    def get_context_data(self, **kwargs: any) -> dict:
        context = super().get_context_data(**kwargs)
        context['title'] = 'Заходи'
        footer_context = {
            'menu': MenuCategory.objects.filter(display=True),
            'footer_events': Event.objects.all().order_by('-date_start')[:2]
        }
        context = {**context, **footer_context}
        return context


class EventDetail(DetailView):
    model = Event
    template_name = 'events-single.html'

    def get_context_data(self, **kwargs: any) -> dict:
        context = super().get_context_data(**kwargs)
        context['title'] = context['object'].title_ukr
        footer_context = {
            'menu': MenuCategory.objects.filter(display=True),
            'footer_events': Event.objects.all().order_by('-date_start')[:2]
        }
        context = {**context, **footer_context}
        return context


class Index(TemplateView):
    template_name = 'index.html'

    def get_context_data(self, **kwargs: any) -> dict:
        context = super().get_context_data(**kwargs)
        context['menu'] = MenuCategory.objects.filter(display=True)
        context['classes'] = Lesson.objects.filter(
            most_popular=True, display=True)
        context['gallery'] = Gallery.objects.filter(most_popular=True)
        context['teachers'] = User.objects.filter(most_popular=True)
        context['events'] = Event.objects.filter(most_popular=True)
        context['drop_down'] = DropDownPoint.objects.filter(main_page=True)
        context['schedule'] = Schedule.objects.all()
        context['comments'] = ParentComment.objects.all()
        context['counters'] = MainCounters.objects.all()
        context['footer_events'] = Event.objects.all().order_by(
            '-date_start')[:2]
        context = {**context}
        return context


class About(TemplateView):
    template_name = 'about.html'

    def get_context_data(self, **kwargs: any) -> dict:
        context = super().get_context_data(**kwargs)
        base_context = {
            'teachers': User.objects.filter(most_popular=True),
            'posts': Post.objects.filter(most_popular=True),
            'drop_down': DropDownPoint.objects.filter(main_page=False),
            'counters': AboutCounters.objects.all(),
        }
        context['title'] = "О нас"
        footer_context = {
            'menu': MenuCategory.objects.filter(display=True),
            'footer_events': Event.objects.all().order_by('-date_start')[:2]
        }
        context = {**context, **base_context, **footer_context}
        return context


class ScheduleView(TemplateView):
    template_name = 'class-schedule.html'

    def get_context_data(self, **kwargs: any) -> dict:
        context = super().get_context_data(**kwargs)
        context['title'] = "Расписание"
        footer_context = {
            'menu': MenuCategory.objects.filter(display=True),
            'footer_events': Event.objects.all().order_by('-date_start')[:2]
        }
        base_context = {'schedule': Schedule.objects.all()}
        context = {**context, **base_context, **
                   footer_context}
        return context


class Contact(FooterContentMixin, TemplateView):
    template_name = 'contact.html'

    def get_context_data(self, **kwargs: any) -> dict:
        context = super().get_context_data(**kwargs)
        context['title'] = "Контакты"
        footer_context = {
            'menu': MenuCategory.objects.filter(display=True),
            'footer_events': Event.objects.all().order_by('-date_start')[:2]
        }
        context = {**context, **footer_context}
        return context


class ComingSoon(FooterContentMixin, TemplateView):
    template_name = 'coming-soon.html'

    def get_context_data(self, **kwargs: any) -> dict:
        context = super().get_context_data(**kwargs)
        context['title'] = "Скоро"
        footer_context = {
            'menu': MenuCategory.objects.filter(display=True),
            'footer_events': Event.objects.all().order_by('-date_start')[:2]
        }
        context = {**context, ** footer_context}
        return context


class FAQ(TemplateView):
    template_name = 'faqs.html'

    def get_context_data(self, **kwargs: any) -> dict:
        context = super().get_context_data(**kwargs)
        base_context = {
            'left': Faq.objects.filter(right=False),
            'right': Faq.objects.filter(right=True),
        }
        context['title'] = "Частые вопросы"
        footer_context = {
            'menu': MenuCategory.objects.filter(display=True),
            'footer_events': Event.objects.all().order_by('-date_start')[:2]
        }
        context = {**context, **base_context, **
                   footer_context}
        return context


class Login(TemplateView):
    template_name = 'login.html'

    def get_context_data(self, **kwargs: any) -> dict:
        context = super().get_context_data(**kwargs)
        context['title'] = "Вход"
        footer_context = {
            'menu': MenuCategory.objects.filter(display=True),
            'footer_events': Event.objects.all().order_by('-date_start')[:2]
        }
        context = {**context, ** footer_context}
        return context


class Registration(TemplateView):
    template_name = 'registration.html'

    def get_context_data(self, **kwargs: any) -> dict:
        context = super().get_context_data(**kwargs)
        context['title'] = "Регистрация"
        footer_context = {
            'menu': MenuCategory.objects.filter(display=True),
            'footer_events': Event.objects.all().order_by('-date_start')[:2]
        }
        context = {**context, ** footer_context}
        return context
