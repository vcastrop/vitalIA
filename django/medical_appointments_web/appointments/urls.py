from django.urls import path, include
from .views import buscar_citas, reservar_cita, appointments_home, results, agendar_cita, ver_mis_citas
from .views import obtener_doctores
from . import views

urlpatterns = [
    path('', appointments_home, name='appointments_home'),  # Página principal de appointments
    path("buscar_citas/", buscar_citas, name="buscar_citas"),
    path("reservar_cita/", reservar_cita, name="reservar_cita"),
    path("obtener_doctores/", obtener_doctores, name="obtener_doctores"),
    path('mis-citas/', ver_mis_citas, name='ver_mis_citas'),
    path("agendar/<int:cita_id>/", agendar_cita, name="agendar_cita"),
]
