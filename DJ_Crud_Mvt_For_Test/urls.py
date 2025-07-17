from django.contrib import admin
from django.urls import path, include
from django.views.generic import TemplateView
from django.utils import timezone

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', TemplateView.as_view(
        template_name='index.html',
        extra_context={'now': timezone.now()}
    ), name='index'),
    path('crud/', include('crud_app.urls')),
    path('mvt/', include('mvt_app.urls')),
]
