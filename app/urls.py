from django.contrib import admin
from django.urls import include, path
from django.conf import settings
from django.conf.urls.static import static
from django.conf.urls import url

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('pdf_generator.urls')),
    path('', include('core.urls')),
    path('questionnaire/', include('questionnaire.urls')),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

if 'survey' in settings.INSTALLED_APPS:
    urlpatterns += [
        url(r'^survey/', include('survey.urls'))
    ]
