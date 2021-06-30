from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from .models import (
    User,
    MenuCategory
)


class UserList(ListView):
    model = User
    context_object_name = 'teachers'
    template_name = 'teacher.html'
    paginate_by = 9

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['menu'] = MenuCategory.objects.all()
        return context


class UserDetail(DetailView):
    model = User
    template_name = 'teacher-single.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['menu'] = MenuCategory.objects.all()
        return context
