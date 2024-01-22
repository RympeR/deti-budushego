from django.contrib import admin
from django.contrib.admin import DateFieldListFilter
from .models import (
    LessonCategory,
    EventCategory,
    Event,
    Lesson,
    Faq,
)


@admin.register(LessonCategory, EventCategory)
class TemplateLessonAdmin(admin.ModelAdmin):
    list_display = 'title_ukr',
    list_display_links = 'title_ukr',
    search_fields = 'title_ukr',

@admin.register(Faq)
class FaqAdmin(admin.ModelAdmin):
    list_display = 'question_ukr', 'short_description', 'right'
    list_display_links = 'question_ukr',
    search_fields = 'question_ukr',
    list_filter = 'right',

@admin.register(Event)
class EventAdmin(admin.ModelAdmin):
    list_display = 'title_ukr', 'small_image', 'organizer', 'timer_time', 'date_end', 'date_start'
    list_display_links = 'title_ukr',
    search_fields = 'title_ukr',
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
    list_display = 'title_ukr', 'small_image', 'teacher', 'class_duration_ukr', 'date_start_ukr', 'display'
    list_display_links = 'title_ukr',
    search_fields = 'title_ukr',
    list_filter = (
        'display',
    )
    filter_horizontal = (
        'tags',
        'related_lessons',
        'related_posts',
        'gallery',
        'category',
    )