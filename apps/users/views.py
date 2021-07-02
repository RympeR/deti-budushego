from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from apps.lessons.models import Event
from .models import (
    User,
    MenuCategory,
    Vacancy
)


class UserList(ListView):
    model = User
    context_object_name = 'teachers'
    template_name = 'teacher.html'
    paginate_by = 9

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['teachers'] = User.objects.filter(teacher=True)
        context['vacancys'] = Vacancy.objects.all()
        context['menu'] = MenuCategory.objects.all()
        context['footer_events'] = Event.objects.all().order_by('-date_start')[:2]
        return context


class UserDetail(DetailView):
    model = User
    template_name = 'teacher-single.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['menu'] = MenuCategory.objects.all()
        context['footer_events'] = Event.objects.all().order_by('-date_start')[:2]
        return context

class VacancyList(ListView):
    model = Vacancy
    context_object_name = 'vacancys'
    template_name = 'vacancys.html'
    paginate_by = 9

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['menu'] = MenuCategory.objects.all()
        context['footer_events'] = Event.objects.all().order_by('-date_start')[:2]
        return context


class VacancyDetail(DetailView):
    model = Vacancy
    template_name = 'vacancy-single.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['menu'] = MenuCategory.objects.all()
        context['footer_events'] = Event.objects.all().order_by('-date_start')[:2]
        return context
