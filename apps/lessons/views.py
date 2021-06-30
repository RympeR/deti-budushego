from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.shortcuts import render
from .models import (
    LessonCategory,
    EventCategory,
    Event,
    Lesson,
)
from apps.users.models import MenuCategory


class LessonList(ListView):
    model = Lesson
    context_object_name = 'lessons'
    template_name = 'classes.html'
    paginate_by = 9

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['categories'] = LessonCategory.objects.all()
        context['menu'] = MenuCategory.objects.all()
        return context


class LessonDetail(DetailView):
    model = Lesson
    template_name = 'class-single.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['menu'] = MenuCategory.objects.all()
        return context


class EventsList(ListView):
    model = Event
    context_object_name = 'events'
    template_name = 'events.html'
    paginate_by = 9

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['categories'] = EventCategory.objects.all()
        context['menu'] = MenuCategory.objects.all()
        return context


class EventDetail(DetailView):
    model = Event
    template_name = 'events-single.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['menu'] = MenuCategory.objects.all()
        return context

def index(request):
    context = {}
    context['menu'] = MenuCategory.objects.all()
    return render(request, 'index.html', context=context)

def about(request):
    context = {}
    context['menu'] = MenuCategory.objects.all()
    return render(request, 'about.html', context=context)

def schedule(request):
    context = {}
    context['menu'] = MenuCategory.objects.all()
    return render(request, 'class-schedule.html', context=context)

def contact(request):
    context = {}
    context['menu'] = MenuCategory.objects.all()
    return render(request, 'contact.html', context=context)

def faq(request):
    context = {}
    context['menu'] = MenuCategory.objects.all()
    return render(request, 'faqs.html', context=context)

def login(request):
    context = {}
    context['menu'] = MenuCategory.objects.all()
    return render(request, 'login.html', context=context)

def registration(request):
    context = {}
    context['menu'] = MenuCategory.objects.all()
    return render(request, 'registration.html', context=context)