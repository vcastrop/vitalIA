from django.contrib import admin
from django.urls import path, include
from django.shortcuts import redirect
from results.views import home  # Importa la vista home

urlpatterns = [
    path("admin/", admin.site.urls),
    path("", home, name="home"),  # Ruta para la página principal
    path("results/", include("results.urls")),  # Ruta para los resultados
]