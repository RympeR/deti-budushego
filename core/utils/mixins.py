from apps.users.models import (
    MenuCategory,
)
from apps.lessons.models import (
    Event,
)
from django.views.generic.base import ContextMixin

class FooterContentMixin(ContextMixin):

    def get_context_data(self, **kwargs: any) -> dict:
        context = super().get_context_data(**kwargs)
        context['menu'] = MenuCategory.objects.filter(display=True)
        context['footer_events'] = Event.objects.all().order_by(
            '-date_start')[:2]
        if hasattr(self, 'base_context'):
            context = {**context, **self.base_context}
        return context