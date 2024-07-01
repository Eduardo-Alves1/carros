
from django.contrib import admin
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from cars.views import CarLitView, NewCarCreateView, CarDatailView
from accounts.views import register_view, login_view, logout_view

urlpatterns = [
    path('admin/', admin.site.urls),
    path('cars/', CarLitView.as_view(), name='cars_list'),
    path('new_car/',NewCarCreateView.as_view(),name='new_car'),
    path('registers/',register_view, name='register'),
    path('login/',login_view, name='login'),
    path('logout/',logout_view, name='logout'),
    path('car/<int:pk>/',CarDatailView.as_view(), name='car_detail'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT) #CONFIGURAÇÃO DE IMAGENS


