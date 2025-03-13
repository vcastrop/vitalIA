from django.contrib import admin
from django.urls import path
from vitalIA_app.views import home, buscar_medicamentos

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', home, name='home'),
    path('buscar-medicamentos/', buscar_medicamentos, name='buscar_medicamentos'),
]