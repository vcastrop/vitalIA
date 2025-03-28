# views.py
from django.shortcuts import render, redirect
from .models import Paciente, Documento

def home(request):
    return render(request, 'vitalia_app/home.html')  # Vista asociada a la ruta ''

def ver_pacientes(request):
    pacientes = Paciente.objects.all()
    return render(request, 'vitalia_app/paciente_list.html', {'pacientes': pacientes})  # Vista asociada a la ruta 'view_patients/'

def confirmar_documentos(request):
    documentos = Documento.objects.all()  # Traemos todos los documentos (pendientes y confirmados)
    return render(request, 'vitalia_app/confirmar_documentos.html', {'documents': documentos})

def confirmar_documento(request, documento_id):
    documento = Documento.objects.get(id=documento_id)
    documento.estado = "Confirmado"  # Cambiamos el estado a "Confirmado"
    documento.save()
    return redirect('confirmar_documentos')  # Redirigimos a la lista de documentos
