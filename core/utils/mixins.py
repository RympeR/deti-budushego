from apps.users.models import (
    MenuCategory,
)
from apps.lessons.models import (
    Event,
)
from django.views.generic.base import ContextMixin

class FooterContentMixin(ContextMixin):
    footer_context = {
        'menu' : MenuCategory.objects.filter(display=True),
        'footer_events' : Event.objects.all().order_by(
            '-date_start')[:2]
    }
    
