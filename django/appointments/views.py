from django.shortcuts import render, get_object_or_404
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
import json
from .models import Cita, Doctor, Especialidad
from datetime import datetime

# Página principal
def home(request):
    especialidades = Especialidad.objects.all()
    return render(request, "home.html", {"especialidades": especialidades})

# Página de resultados
def results(request):
    return render(request, 'results.html', {'appointments': []})

# Obtener doctores según especialidad
def obtener_doctores(request):
    especialidad_id = request.GET.get("especialidad_id")
    doctores = Doctor.objects.filter(especialidad_id=especialidad_id)
    data = {"doctores": [{"id": doc.id, "nombre": doc.nombre} for doc in doctores]}
    return JsonResponse(data)

# Buscar citas disponibles
def buscar_citas(request):
    if request.method == "GET":
        fecha = request.GET.get("fecha")
        especialidad = request.GET.get("especialidad")
        doctor = request.GET.get("doctor")  # Obtener el ID del doctor

        if fecha and especialidad and doctor:
            try:
                fecha_convertida = datetime.strptime(fecha, "%Y-%m-%d").date()
                citas = Cita.objects.filter(
                    fecha=fecha_convertida,
                    especialidad__id=especialidad,
                    doctor__id=doctor,
                    disponible=True
                )

                citas_json = [
                    {"id": cita.id, "fecha": cita.fecha.strftime("%d/%m/%Y"), "hora": cita.hora.strftime("%H:%M")}
                    for cita in citas
                ]

                return JsonResponse({"citas": citas_json})

            except ValueError:
                return JsonResponse({"error": "Formato de fecha inválido"}, status=400)

    return JsonResponse({"error": "Parámetros incorrectos"}, status=400)

# Agendar cita (Marcar como ocupada)
@csrf_exempt
def agendar_cita(request, cita_id):
    if request.method == "POST":
        try:
            cita = get_object_or_404(Cita, id=cita_id)

            if not cita.disponible:
                return JsonResponse({"error": "La cita ya fue ocupada."}, status=400)

            cita.disponible = False
            cita.save()

            return JsonResponse({"mensaje": "Cita agendada correctamente."}, status=200)

        except Exception as e:
            return JsonResponse({"error": str(e)}, status=500)

    return JsonResponse({"error": "Método no permitido."}, status=405)

@csrf_exempt
def reservar_cita(request):
    if request.method == "POST":
        try:
            data = json.loads(request.body)
            cita_id = data.get("cita_id")

            if not cita_id:
                return JsonResponse({"mensaje": "ID de cita no proporcionado."}, status=400)

            cita = Cita.objects.get(id=cita_id)

            if not cita.disponible:
                return JsonResponse({"mensaje": "La cita ya está ocupada."}, status=400)

            cita.disponible = False  # Marcar la cita como ocupada
            cita.save()

            return JsonResponse({"mensaje": "Cita agendada correctamente."}, status=200)

        except Cita.DoesNotExist:
            return JsonResponse({"mensaje": "La cita no existe."}, status=404)
        except Exception as e:
            return JsonResponse({"mensaje": f"Error: {str(e)}"}, status=500)

    return JsonResponse({"mensaje": "Método no permitido."}, status=405)