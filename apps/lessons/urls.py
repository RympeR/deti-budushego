from django.urls import path
from .views import (
    LessonList,
    LessonDetail,
    EventsList,
    EventDetail,
    Index,
    About,
    ScheduleView,
    Contact,
    FAQ,
    Login,
    Registration,
    ComingSoon,
    EventsListFiltered,
    LessonListFiltered,
    LessonListFilteredByTag,
)

app_name = 'lessons_section'

urlpatterns = [
    path('classes/', LessonList.as_view(), name='lessons_list'),
    path('classes/<slug:slug>', LessonDetail.as_view(), name='lesson_detail'),
    path('classes-filtered/<slug:slug>', LessonListFiltered.as_view(), name='lesson_list_filtered'),
    path('classes-filtered-ages/<slug:slug>', LessonListFilteredByTag.as_view(), name='lesson_list_filtered_ages'),
    path('events/<slug:slug>', EventDetail.as_view(), name='event_detail'),
    path('events/', EventsList.as_view(), name='events_list'),
    path('events-filtered/<slug:slug>', EventsListFiltered.as_view(), name='events_list_filtered'),
    path('', Index.as_view(), name='index'),
    path('about/', About.as_view(), name='about'),
    path('schedule/', ScheduleView.as_view(), name='schedule'),
    path('contact/', Contact.as_view(), name='contact'),
    path('coming_soon/', ComingSoon.as_view(), name='coming_soon'),
    path('faq/', FAQ.as_view(), name='faq'),
    path('login/', Login.as_view(), name='login'),
    path('registration/', Registration.as_view(), name='registration'),

]
