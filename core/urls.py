from apps.users.views import switch_to_Russian_link, switch_to_Ukraiunian_link
from django.conf import settings
from django.conf.urls.i18n import i18n_patterns
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import include, path
from django.views.generic.base import TemplateView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('uk-switch/', switch_to_Ukraiunian_link, name='uk'),
    path('ru-switch/', switch_to_Russian_link, name='ru'),
    path(
        "robots.txt",
        TemplateView.as_view(template_name="robots.txt",
                             content_type="text/plain"),
    ),
    path('i18n/', include('django.conf.urls.i18n')),
    path('ckeditor/', include('ckeditor_uploader.urls')),
]
urlpatterns += i18n_patterns(
    path('', include('apps.users.urls')),
    path('', include('apps.lessons.urls')),
    path('', include('apps.blog.urls')),
    path('', include('apps.ecommerce.urls')),
)
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

handler404 = 'apps.lessons.views.handler404'
handler500 = 'apps.lessons.views.handler500'
