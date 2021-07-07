from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.shortcuts import render
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
from apps.blog.models import Gallery, Post


class LessonList(ListView):
    model = Lesson
    context_object_name = 'lessons'
    template_name = 'classes.html'
    paginate_by = 9

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['categories'] = LessonCategory.objects.all()
        context['menu'] = MenuCategory.objects.filter(display=True)
        context['footer_events'] = Event.objects.all().order_by('-date_start')[:2]
        return context


class LessonDetail(DetailView):
    model = Lesson
    template_name = 'class-single.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['menu'] = MenuCategory.objects.filter(display=True)
        context['footer_events'] = Event.objects.all().order_by('-date_start')[:2]
        return context


class EventsList(ListView):
    model = Event
    context_object_name = 'events'
    template_name = 'events.html'
    paginate_by = 9

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['categories'] = EventCategory.objects.all()
        context['menu'] = MenuCategory.objects.filter(display=True)
        context['footer_events'] = Event.objects.all().order_by('-date_start')[:2]
        return context


class EventDetail(DetailView):
    model = Event
    template_name = 'events-single.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['menu'] = MenuCategory.objects.filter(display=True)
        context['footer_events'] = Event.objects.all().order_by('-date_start')[:2]
        return context


def index(request):
    context = dict()
    context['menu'] = MenuCategory.objects.filter(display=True)
    context['classes'] = Lesson.objects.filter(most_popular=True)
    context['gallery'] = Gallery.objects.filter(most_popular=True)
    context['teachers'] = User.objects.filter(most_popular=True)
    context['events'] = Event.objects.filter(most_popular=True)
    context['drop_down'] = DropDownPoint.objects.filter(main_page=True)
    context['schedule'] = Schedule.objects.all()
    context['footer_events'] = Event.objects.all().order_by('-date_start')[:2]
    context['comments'] = ParentComment.objects.all()
    context['counters'] = MainCounters.objects.all()

    return render(request, 'index.html', context=context)


def about(request):
    context = dict()
    context['menu'] = MenuCategory.objects.filter(display=True)
    context['teachers'] = User.objects.filter(most_popular=True)
    context['posts'] = Post.objects.filter(most_popular=True)
    context['drop_down'] = DropDownPoint.objects.filter(main_page=False)
    context['footer_events'] = Event.objects.all().order_by('-date_start')[:2]
    context['counters'] = AboutCounters.objects.all()
    return render(request, 'about.html', context=context)


def schedule(request):
    context = dict()
    context['menu'] = MenuCategory.objects.filter(display=True)
    context['schedule'] = Schedule.objects.all()
    context['footer_events'] = Event.objects.all().order_by('-date_start')[:2]
    return render(request, 'class-schedule.html', context=context)


def contact(request):
    context = dict()
    context['menu'] = MenuCategory.objects.filter(display=True)
    context['footer_events'] = Event.objects.all().order_by('-date_start')[:2]
    return render(request, 'contact.html', context=context)


def coming_soon(request):
    context = dict()
    context['menu'] = MenuCategory.objects.filter(display=True)
    context['footer_events'] = Event.objects.all().order_by('-date_start')[:2]
    return render(request, 'coming-soon.html', context=context)


def faq(request):
    context = dict()
    context['menu'] = MenuCategory.objects.filter(display=True)
    context['left'] = Faq.objects.filter(right=False)
    context['right'] = Faq.objects.filter(right=True)
    context['footer_events'] = Event.objects.all().order_by('-date_start')[:2]
    return render(request, 'faqs.html', context=context)


def login(request):
    context = dict()
    context['menu'] = MenuCategory.objects.filter(display=True)
    context['footer_events'] = Event.objects.all().order_by('-date_start')[:2]
    return render(request, 'login.html', context=context)


def registration(request):
    context = dict()
    context['menu'] = MenuCategory.objects.filter(display=True)
    context['footer_events'] = Event.objects.all().order_by('-date_start')[:2]
    return render(request, 'registration.html', context=context)
