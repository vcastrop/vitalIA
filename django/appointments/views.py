from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404
from .models import Cita
from django.http import JsonResponse
from appointments.models import Cita, Especialidad
from datetime import datetime
from .models import Doctor

# Create your views here.

def home(request):
    especialidades = Especialidad.objects.all()
    return render(request, "home.html", {"especialidades": especialidades})

def results(request):
    return render(request, 'results.html', {'appointments': []})


def obtener_doctores(request):
    especialidad_id = request.GET.get("especialidad_id")
    doctores = Doctor.objects.filter(especialidad_id=especialidad_id)

    data = {"doctores": [{"id": doc.id, "nombre": doc.nombre} for doc in doctores]}

    return JsonResponse(data)

def buscar_citas(request):
    if request.method == "GET":
        fecha = request.GET.get("fecha")
        especialidad = request.GET.get("especialidad")
        doctor = request.GET.get("doctor")  # Obtener el ID del doctor

        if fecha and especialidad and doctor:
            try:
                # Convertir la fecha correctamente
                fecha_convertida = datetime.strptime(fecha, "%Y-%m-%d").date()

                # Filtrar citas por fecha, especialidad y doctor
                citas = Cita.objects.filter(
                    fecha=fecha_convertida,
                    especialidad__id=especialidad,
                    doctor__id=doctor,  # Filtrar por doctor
                    disponible=True
                )

                citas_json = [
                    {"fecha": cita.fecha.strftime("%d/%m/%Y"), "hora": cita.hora.strftime("%H:%M")}
                    for cita in citas
                ]

                return JsonResponse({"citas": citas_json})

            except ValueError:
                return JsonResponse({"error": "Formato de fecha inválido"}, status=400)

    return JsonResponse({"error": "Parámetros incorrectos"}, status=400)

def reservar_cita(request):
    return JsonResponse({"mensaje": "Función de reservar cita aún no implementada"})
