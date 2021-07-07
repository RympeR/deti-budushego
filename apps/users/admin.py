from django.contrib import admin, messages
from mptt.admin import TreeRelatedFieldListFilter, DraggableMPTTAdmin
from django.http import HttpResponseRedirect
from django.contrib.admin import DateFieldListFilter
from django.urls import reverse, reverse_lazy
from admin_actions.admin import ActionsModelAdmin
from .models import (
    MenuCategory,
    Attachments,
    User,
    Program,
    Schedule,
    Vacancy,
    ParentComment,
    MainCounters,
    AboutCounters,
    DropDownPoint,
)

@admin.register(DropDownPoint)
class DropDownPointAdmin(admin.ModelAdmin):
    list_display = 'title', 'short_description', 'main_page'
    list_display_links = 'title',
    list_filter = 'main_page', 'opened'
    search_fields = 'title',


@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    list_display = 'username', 'fio', 'user_photo'
    list_display_links = 'username',
    search_fields = 'username', 'fio',
    fieldsets = (

        ('Личная информация', {
            'fields': ('username', 'fio', 'image')
        }),
        ('Дополнительная информация', {
            'fields': ('specialization', 'personal_statement', 'characteristic', 'sertificates')
        }),
        ('Информация для сайта', {
            'fields': ('slug','most_popular', 'teacher')
        }),

    )


@admin.register(Attachments)
class AttachemntsAdmin(admin.ModelAdmin):
    list_display = 'pk', 'attachment_type', 'attachment'
    list_display_links = 'pk',
    filter_fields ='attachment_type',


@admin.register(Vacancy)
class VacancyAdmin(admin.ModelAdmin):
    list_display = 'name', 'vacancy_photo'
    list_display_links = 'name',
    search_fields ='name',


@admin.register(MenuCategory)
class MenuCategoryAdmin(DraggableMPTTAdmin):
    list_display = 'tree_actions', 'name', 'display'
    list_display_links = 'name',
    filter_fields = 'display',
    search_fields = 'name',
    list_filter = (
        ('parent', TreeRelatedFieldListFilter),
    )


@admin.register(Program)
class ProgramAdmin(admin.ModelAdmin):
    list_display = 'name', 'hours'
    list_display_links = 'name',
    search_fields = 'name',


@admin.register(Schedule)
class ScheduleAdmin(admin.ModelAdmin):
    list_display = 'pk', 'schedule_photo'
    list_display_links = 'pk',
    filter_horizontal = 'programs',


@admin.register(ParentComment)
class ParentCommentAdmin(admin.ModelAdmin):
    list_display = 'parent_name', 'short_comment'
    list_display_links = 'parent_name',
    search_fields = 'parent_name',


@admin.register(MainCounters, AboutCounters)
class MainCountersAdmin(admin.ModelAdmin):
    list_display = 'amount', 'description'
    list_display_links = 'description',
