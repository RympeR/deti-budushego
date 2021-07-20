from django.contrib import admin
from django.contrib.admin import DateFieldListFilter
from .models import (
    Category,
    Product,
    Order,
    OrderItem,
    Payment,
    Coupon,
)


@admin.register(Coupon)
class CouponAdmin(admin.ModelAdmin):
    list_display = 'code', 'discount_percent', 'amount'
    list_display_links = 'code',
    search_fields = 'code',


@admin.register(Payment)
class PaymentAdmin(admin.ModelAdmin):
    list_display = 'pk', 'order', 'amount', 'timestamp'
    list_display_links = 'pk',
    list_filter = (
        ('timestamp', DateFieldListFilter),
    )


@admin.register(OrderItem)
class OrderItemAdmin(admin.ModelAdmin):
    list_display = 'pk', 'order', 'product',
    list_display_links = 'pk',
    search_fields = 'product__title',


@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    list_display = 'pk', 'user', 'start_date', 'coupon', 'finished'
    list_display_links = 'pk',
    search_fields = 'user__fio',
    list_filter = (
        ('start_date', DateFieldListFilter),
        'finished',
    )


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = 'name', 'slug', 
    list_display_links = 'name',
    search_fields = 'name',



@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = 'title', 'admin_preview', 'created_at'
    list_display_links = 'title',
    search_fields = 'title', 
    list_filter = (
        ('created_at', DateFieldListFilter),
        'category',
    )
    filter_horizontal = 'attachments',
