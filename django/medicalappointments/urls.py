from django.contrib import admin
from django.urls import path, include
from django.shortcuts import redirect
urlpatterns = [
    path('', lambda request: redirect('/citas/')),
    path('admin/', admin.site.urls),
    path('citas/', include('appointments.urls')),  # Incluir las rutas de la app appointments
]
