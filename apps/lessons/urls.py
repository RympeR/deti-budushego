from django.urls import path
from .views import (
    LessonList,
    LessonDetail,
    EventsList,
    EventDetail,
    index,
    about,
    schedule,
    contact,
    faq,
    login,
    registration,
)

app_name = 'lessons_section'

urlpatterns = [
    path('lessons/', LessonList.as_view(), name='lessons_list'),
    path('lesson/<slug:slug>', LessonDetail.as_view(), name='lesson_detail'),
    path('event/<slug:slug>', EventDetail.as_view(), name='event_detail'),
    path('events/', EventsList.as_view(), name='events_list'),
    path('', index, name='index'),
    path('about/', about, name='about'),
    path('schedule/', schedule, name='schedule'),
    path('contact/', contact, name='contact'),
    path('faq/', faq, name='faq'),
    path('login/', login, name='login'),
    path('registration/', registration, name='registration'),

]
