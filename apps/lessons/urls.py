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
    coming_soon,
    EventsListFiltered,
    LessonListFiltered,
)

app_name = 'lessons_section'

urlpatterns = [
    path('classes/', LessonList.as_view(), name='lessons_list'),
    path('classes/<slug:slug>', LessonDetail.as_view(), name='lesson_detail'),
    path('classes-filtered/<slug:slug>', LessonListFiltered.as_view(), name='lesson_list_filtered'),
    path('events/<slug:slug>', EventDetail.as_view(), name='event_detail'),
    path('events/', EventsList.as_view(), name='events_list'),
    path('events-filtered/<slug:slug>', EventsListFiltered.as_view(), name='events_list_filtered'),
    path('', index, name='index'),
    path('about/', about, name='about'),
    path('schedule/', schedule, name='schedule'),
    path('contact/', contact, name='contact'),
    path('coming_soon/', coming_soon, name='coming_soon'),
    path('faq/', faq, name='faq'),
    path('login/', login, name='login'),
    path('registration/', registration, name='registration'),

]
