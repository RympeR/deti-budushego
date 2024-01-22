from django.contrib import admin, messages
from mptt.admin import TreeRelatedFieldListFilter, DraggableMPTTAdmin
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
class DropDownPointAdmin(DraggableMPTTAdmin):
    list_display = 'tree_actions', 'title_ukr', 'short_description', 'main_page'
    list_display_links = 'title_ukr',
    list_filter = 'main_page', 'opened'
    search_fields = 'title_ukr',
    fields = 'title_ukr', 'description_ukr', 'main_page', 'opened'

@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    list_display = 'username', 'fio_ukr', 'user_photo'
    list_display_links = 'username',
    search_fields = 'username', 'fio_ukr',
    fieldsets = (

        ('Личная информация', {
            'fields': ('username', 'fio_ukr', 'image')
        }),
        ('Дополнительная информация', {
            'fields': (
            'specialization_ukr', 
            'personal_statement_ukr',
            'characteristic_ukr',
            'sertificates')
        }),
        ('Информация для сайта', {
            'fields': ('slug','most_popular', 'teacher')
        }),
    )
    filter_horizontal = 'sertificates',


@admin.register(Attachments)
class AttachemntsAdmin(admin.ModelAdmin):
    list_display = 'pk', 'attachment_type', 'attachment'
    list_display_links = 'pk',
    list_filter ='attachment_type',


@admin.register(Vacancy)
class VacancyAdmin(admin.ModelAdmin):
    list_display = 'name_ukr', 'vacancy_photo'
    list_display_links = 'name_ukr',
    search_fields ='name_ukr',


@admin.register(MenuCategory)
class MenuCategoryAdmin(DraggableMPTTAdmin):
    list_display = 'tree_actions', 'name_ukr', 'display'
    list_display_links = 'name_ukr',
    filter_fields = 'display',
    search_fields = 'name_ukr',
    list_filter = (
        ('parent', TreeRelatedFieldListFilter),
    )


@admin.register(Program)
class ProgramAdmin(admin.ModelAdmin):
    list_display = 'name_ukr', 'hours_ukr'
    list_display_links = 'name_ukr',
    search_fields = 'name_ukr',


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
    list_display = 'amount', 'description_ukr'
    list_display_links = 'description_ukr',
