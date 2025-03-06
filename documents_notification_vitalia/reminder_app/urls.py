from django.urls import path
from . import views

urlpatterns = [
    path('', views.reminder, name='reminder'),  # Ruta base para listar los recordatorios
]