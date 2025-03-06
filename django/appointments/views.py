from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404
from .models import Cita
from django.http import JsonResponse
from appointments.models import Cita, Especialidad
from datetime import datetime

# Create your views here.

def home(request):
    especialidades = Especialidad.objects.all()
    return render(request, "home.html", {"especialidades": especialidades})

def results(request):
    return render(request, 'results.html', {'appointments': []})



def buscar_citas(request):
    if request.method == "GET":
        fecha = request.GET.get("fecha")
        especialidad = request.GET.get("especialidad")

        if fecha and especialidad:
            citas = Cita.objects.filter(fecha=fecha, especialidad__nombre=especialidad, disponible=True)
            citas_json = [{"fecha": cita.fecha, "hora": cita.hora} for cita in citas]

            return JsonResponse({"citas": citas_json})

    return JsonResponse({"error": "Parámetros incorrectos"}, status=400)


def reservar_cita(request, cita_id):
    cita = get_object_or_404(Cita, id=cita_id)
    cita.disponible = False
    cita.save()
    return render(request, "appointments/reserva_exitosa.html", {"cita": cita})