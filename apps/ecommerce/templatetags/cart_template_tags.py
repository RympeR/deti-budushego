from apps.ecommerce.models import *
from django import template
from django.db.models import Q
from apps.blog.models import *
from apps.lessons.models import *
from apps.users.models import *

register = template.Library()

@register.filter
def shop_categories(request):
    qs = Category.objects.all()
    if qs.exists():
        return qs
    return []

@register.filter
def latest_products(request):
    qs = Product.objects.all().order_by('-pk')[:3]
    if qs.exists():
        return qs
    return []
    
@register.filter
def cart_item_count(request):
    if request.user.is_authenticated:
        user = request.user
        try:
            qs = Order.objects.get(Q(finished=False) & Q(user=user))
        except Exception:
            return 0
        if qs:
            try:
                return qs.items_order.count()
            except:
                return 0
    return 0
    
@register.filter
def cart_products(request):
    if request.user.is_authenticated:
        user = request.user
        try:
            qs = Order.objects.get(Q(finished=False) & Q(user=user))
        except Exception:
            return []
        if qs:
            order_items = qs.items_order.all()
            products = [ item.product for item in order_items ]
            return products
    return []

@register.filter
def post_categories(request):
    qs = PostCategory.objects.all()
    if qs.exists():
        return qs
    return []

@register.filter
def gallery_categories(request):
    qs = GalleryCategory.objects.all()
    if qs.exists():
        return qs
    return []

@register.filter
def lesson_categories(request):
    qs = LessonCategory.objects.all()
    if qs.exists():
        return qs
    return []

@register.filter
def events_categories(request):
    qs = EventCategory.objects.all()
    if qs.exists():
        return qs
    return []
