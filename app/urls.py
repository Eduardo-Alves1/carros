
from django.contrib import admin
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from cars.views import cars_viwe, new_car_view
from accounts.views import register_view

urlpatterns = [
    path('admin/', admin.site.urls),
    path('cars/', cars_viwe, name='cars_list'),
    path('new_car/',new_car_view, name='new_car'),
    path('registers/',register_view, name='register'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT) #CONFIGURAÇÃO DE IMAGENS


