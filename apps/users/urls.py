from django.urls import path
from .views import (
    UserList,
    UserDetail,
    VacancyDetail,
    VacancyList,
    register,
    loginView,
    logoutView,
    CustomerDetail,
    switch_to_Russian_link,
    switch_to_Ukraiunian_link,
)

from django.conf import settings
app_name = 'users_section'

urlpatterns = [
    path('teachers/', UserList.as_view(), name='teachers_list'),
    path('register/', register, name='register'),
    path('logout/', logoutView, name='logout'),
    path('login/', loginView, name='login'),
    path('teachers/<slug:slug>', UserDetail.as_view(), name='teacher_detail'),
    path('profile/', CustomerDetail.as_view(), name='profile_detail'),
    path('vacancys/', VacancyList.as_view(), name='vacancy_list'),
    path('vacancys/<slug:slug>', VacancyDetail.as_view(), name='vacancy_detail'),
]
