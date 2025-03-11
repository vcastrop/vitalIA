from django.urls import path
from .views import buscar_citas, reservar_cita, home, results, agendar_cita
from .views import obtener_doctores

urlpatterns = [
    path('', home, name='home'),
    path('results/', results, name='results'),
    path("buscar_citas/", buscar_citas, name="buscar_citas"),
    path("reservar_cita/", reservar_cita, name="reservar_cita"),
    path("obtener_doctores/", obtener_doctores, name="obtener_doctores"),
    path("agendar/<int:cita_id>/", agendar_cita, name="agendar_cita"),
]
