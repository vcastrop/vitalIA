from django.urls import path
from .views import buscar_citas, reservar_cita, home, results
from .views import obtener_doctores

urlpatterns = [
    path('', home, name='home'),
    path('results/', results, name='results'),
    path("buscar_citas/", buscar_citas, name="buscar_citas"),
    path("reservar/<int:cita_id>/", reservar_cita, name="reservar_cita"),
    path("obtener_doctores/", obtener_doctores, name="obtener_doctores"),
]
