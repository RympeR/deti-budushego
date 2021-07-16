from apps.ecommerce.models import *
from django import template


register = template.Library()

@register.filter
def shop_categories(request):
    qs = Category.objects.all()
    if qs.exists():
        return qs
    return 0

@register.filter
def latest_products(request):
    qs = Product.objects.all().order_by('-pk')[:3]
    if qs.exists():
        return qs
    return 0
    
@register.filter
def cart_item_count(request):
    if request.user.is_authenticated:
        user = request.user
        qs = Order.objects.filter(finished=False, user=user)
        if qs.exists():
            try:
                return qs[0].items_order.count()
            except:
                return 0
    return 0
