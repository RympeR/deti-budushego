from django.contrib import admin
from django.contrib.admin import DateFieldListFilter
from .models import (
    LessonCategory,
    EventCategory,
    Event,
    Lesson,
)


@admin.register(LessonCategory, EventCategory)
class TemplateLessonAdmin(admin.ModelAdmin):
    list_display = 'title',
    list_display_links = 'title',
    search_fields = 'title',


@admin.register(Event)
class EventAdmin(admin.ModelAdmin):
    list_display = 'title', 'small_image', 'organizer', 'timer_time', 'date_end', 'date_start'
    list_display_links = 'title',
    filter_fields = 'timer_time', 'date_end', 'date_start'
    search_fields = 'name',
    list_filter = (
        ('timer_time', DateFieldListFilter),
        ('date_end', DateFieldListFilter),
        ('date_start', DateFieldListFilter),
    )
    filter_horizontal = (
        'related_posts',
        'gallery',
        'tags',
        'category',
    )


@admin.register(Lesson)
class LessonAdmin(admin.ModelAdmin):
    list_display = 'title', 'small_image', 'teacher', 'class_duration', 'date_start'
    list_display_links = 'title',
    filter_fields = 'class_duration', 'date_start'
    search_fields = 'name',
    list_filter = (
        ('class_duration', DateFieldListFilter),
        ('date_start', DateFieldListFilter),
    )
    filter_horizontal = (
        'tags',
        'related_lessons',
        'related_posts',
        'gallery',
        'category',
    )