from django.contrib import admin
from django.urls import path, include
from django.views.generic import TemplateView
from django.utils import timezone

urlpatterns = [
    path('admin/', admin.site.urls),

    # Главная страница проекта
    path('', TemplateView.as_view(
        template_name='index.html',
        extra_context={'now': timezone.now()}
    ), name='index'),

    # Ведём на index CRUD‑приложения
    path('crud/', include('crud_app.urls')),

    # Ведём на index MVT‑приложения
    path('mvt/', include('mvt_app.urls')),
]
