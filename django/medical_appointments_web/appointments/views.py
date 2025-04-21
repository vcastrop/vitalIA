from django.shortcuts import render, get_object_or_404
from django.http import JsonResponse
from django.views.decorators.http import require_POST
from django.views.decorators.csrf import csrf_exempt
import json
from .models import Cita, Doctor, Especialidad
from datetime import datetime
from django.contrib.auth.decorators import login_required
# Página principal


@login_required
def ver_mis_citas(request):
    citas = Cita.objects.filter(usuario=request.user).order_by('fecha', 'hora')
    return render(request, 'mi_cita.html', {'citas': citas})

def appointments_home(request):
    especialidades = Especialidad.objects.all()
    doctores = Doctor.objects.all()

    return render(request, "homeAppointments.html", {
        "especialidades": especialidades,
        "doctores": doctores
    })

# Página de resultados
def results(request):
    return render(request, 'home.html', {'appointments': []})


# Obtener doctores según especialidad

def obtener_doctores(request):
    especialidad_id = request.GET.get("especialidad_id")
    if especialidad_id:
        doctores = Doctor.objects.filter(especialidad_id=especialidad_id).values("id", "nombre")
        return JsonResponse({"doctores": list(doctores)})
    return JsonResponse({"doctores": []})

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

@login_required
@csrf_exempt
def reservar_cita(request):
    try:
        data = json.loads(request.body)
        cita_id = data.get("cita_id")

        if not cita_id:
            return JsonResponse({"mensaje": "ID de cita no proporcionado."}, status=400)

        cita = Cita.objects.get(id=cita_id)

        if not cita.disponible:
            return JsonResponse({"mensaje": "La cita ya está ocupada."}, status=400)

        # 👇 Aquí es donde se asigna el usuario a la cita
        cita.disponible = False
        cita.usuario = request.user
        cita.save()

        return JsonResponse({"mensaje": "Cita agendada correctamente."}, status=200)

    except Cita.DoesNotExist:
        return JsonResponse({"mensaje": "La cita no existe."}, status=404)
    except Exception as e:
        return JsonResponse({"mensaje": f"Error: {str(e)}"}, status=500)