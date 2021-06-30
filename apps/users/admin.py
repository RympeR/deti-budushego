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
)

@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    list_display = 'username', 'fio', 'email', 'user_photo'
    list_display_links = 'username',
    search_fields = 'username', 'fio', 'email'

@admin.register(Attachments)
class AttachemntsAdmin(admin.ModelAdmin):
    list_display = 'pk', 'attachment_type'
    list_display_links = 'pk',
    filter_fields ='attachment_type',

@admin.register(MenuCategory)
class MenuCategoryAdmin(DraggableMPTTAdmin):
    list_display = 'tree_actions', 'name', 'display'
    list_display_links = 'name',
    filter_fields = 'display',
    search_fields = 'name',
    list_filter = (
        ('parent', TreeRelatedFieldListFilter),
    )
