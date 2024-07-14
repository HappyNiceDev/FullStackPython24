from django.urls import path, include
from . import views
from django.contrib.auth import views as auth_views
from django.conf.urls.static import static
from django.conf import settings
from .views import eliminar_cuenta

urlpatterns = [
    path('', views.index, name='index'),
    path('cuentaconfig/', views.cuentaconfig, name='cuentaconfig'),
    path('register/', views.register, name='register'),
    path('eliminar_cuenta/', eliminar_cuenta, name='eliminar_cuenta'),
    
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)