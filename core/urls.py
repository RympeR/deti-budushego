from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from django.views.generic.base import TemplateView
from django.conf.urls.i18n import i18n_patterns

urlpatterns = [
    path('admin/', admin.site.urls),
]
urlpatterns += i18n_patterns(
    path('', include('apps.users.urls')),
    path('', include('apps.lessons.urls')),
    path('', include('apps.blog.urls')),
    path('', include('apps.ecommerce.urls')),
    path('ckeditor/', include('ckeditor_uploader.urls')),
    path(
        "robots.txt",
        TemplateView.as_view(template_name="robots.txt",
                             content_type="text/plain"),
    ),
    prefix_default_language=False,
)
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

handler404 = 'apps.lessons.views.handler404'
handler500 = 'apps.lessons.views.handler500'
