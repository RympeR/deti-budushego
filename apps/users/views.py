from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import HttpResponse
from django.shortcuts import get_object_or_404, redirect, render
from django.views.generic.detail import DetailView
from django.views.generic.list import ListView

from apps.ecommerce.models import Product
from apps.lessons.models import Event

from .forms import RegisterForm, UserLoginForm
from .models import MenuCategory, User, Vacancy
from core.utils.mixins import (
    FooterContentMixin,
)


def switch_to_Russian_link(request):
    request.session['lang'] = 'ru'
    return HttpResponse('switched to russian')


def switch_to_Ukraiunian_link(request):
    request.session['lang'] = 'uk'
    return HttpResponse('switched to ukrainian ')


class UserList(ListView):
    model = User
    context_object_name = 'teachers'
    template_name = 'teacher.html'
    paginate_by = 9

    def get_context_data(self, **kwargs: any) -> dict:
        context = super().get_context_data(**kwargs)
        base_context = {
            'teachers': User.objects.filter(teacher=True),
            'vacancys': Vacancy.objects.all(),
        }
        context['title'] = 'Преподаватели'
        footer_context = {
            'menu' : MenuCategory.objects.filter(display=True),
            'footer_events' : Event.objects.all().order_by(
                '-date_start')[:2]
        }
        context = {**context, **base_context, **
                   footer_context}
        return context


class UserDetail(DetailView):
    model = User
    template_name = 'teacher-single.html'

    def get_context_data(self, **kwargs: any) -> dict:
        context = super().get_context_data(**kwargs)
        context['title'] = context['object'].fio
        footer_context = {
            'menu' : MenuCategory.objects.filter(display=True),
            'footer_events' : Event.objects.all().order_by(
                '-date_start')[:2]
        }
        context = {**context, **footer_context}
        return context

# @login_required(login_url='/login/')


class CustomerDetail(LoginRequiredMixin, ListView):
    model = Product
    template_name = 'profile.html'
    context_object_name = 'products'
    login_url = '/login/'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['user'] = self.request.user
        context['menu'] = MenuCategory.objects.filter(display=True)
        context['footer_events'] = Event.objects.all().order_by(
            '-date_start')[:2]
        products = Product.objects.all()
        products = [
            product for product in products if product.check_bought() == True]

        context['products'] = products
        context['title'] = 'Заказы'
        return context


class VacancyList(ListView):
    model = Vacancy
    context_object_name = 'vacancys'
    template_name = 'vacancys.html'
    paginate_by = 9

    def get_context_data(self, **kwargs: any) -> dict:
        context = super().get_context_data(**kwargs)
        footer_context = {
            'menu' : MenuCategory.objects.filter(display=True),
            'footer_events' : Event.objects.all().order_by(
                '-date_start')[:2]
        }
        context = {**context, **footer_context}
        context['title'] = 'Список вакансий'
        return context


class VacancyDetail(DetailView):
    model = Vacancy
    template_name = 'vacancy-single.html'
    
    def get_context_data(self, **kwargs: any) -> dict:
        context = super().get_context_data(**kwargs)
        context['title'] = 'Вакансия'
        return context


def register(request):
    if request.user.is_authenticated:
        return redirect('lessons_section:index')
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            form.save()
            new_user = authenticate(username=form.cleaned_data['username'],
                                    password=form.cleaned_data['password1'],
                                    )
            login(request, new_user)
            return redirect('lessons_section:index')
    context = {}
    context['menu'] = MenuCategory.objects.filter(display=True)
    context['form'] = RegisterForm()
    context['title'] = 'Регистрация'
    context['footer_events'] = Event.objects.all().order_by('-date_start')[:2]
    footer_context = {
            'menu' : MenuCategory.objects.filter(display=True),
            'footer_events' : Event.objects.all().order_by(
                '-date_start')[:2]
        }
    context = {**context,**footer_context}
    return render(request, 'registration.html', context)


def loginView(request):
    if request.user.is_authenticated:
        return redirect('lessons_section:index')
    else:
        print("Not logged in")
    if request.method == 'POST':
        form = UserLoginForm(data=request.POST)
        if form.is_valid():
            new_user = authenticate(username=form.cleaned_data['username'],
                                    password=form.cleaned_data['password'],
                                    )
            login(request, new_user)
            return redirect('lessons_section:index')
        else:
            result = {
                "status": "error",
                "errors": form.errors
            }
            # messages.debug(request, 'Неверный логин или пароль')
            # return HttpResponse(json.dumps(result),
            #             content_type ="application/json")
    context = {}
    context['menu'] = MenuCategory.objects.filter(display=True)
    context['form'] = UserLoginForm()
    context['footer_events'] = Event.objects.all().order_by('-date_start')[:2]
    context['title'] = 'Вход'

    return render(request, 'login.html', context)


def logoutView(request):
    if request.user.is_authenticated:
        logout(request)
        return redirect('lessons_section:index')
    else:
        return redirect('lessons_section:login')
