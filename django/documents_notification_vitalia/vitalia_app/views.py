# views.py
from django.shortcuts import render, redirect, get_object_or_404
from .models import Paciente, Documento
from django.apps import apps
import json
from django.contrib.auth.decorators import login_required

@login_required
def inicio(request):
    return render(request, 'vitalia_app/home.html')  # Vista asociada a la ruta ''

@login_required
def ver_documentos_confirmados(request):
    # Obtener todos los documentos confirmados
    documentos_confirmados = Documento.objects.filter(estado='confirmado', reminder__user=request.user).order_by('-fecha_confirmacion')
    
    return render(request, 'vitalia_app/documentos_confirmados.html', {
        'documentos': documentos_confirmados
    })

@login_required
def confirmar_documentos(request):
    # Obtener el modelo Reminder dinámicamente
    Reminder = apps.get_model('reminder_app', 'Reminder')
    
    # Obtener todos los recordatorios activos
    recordatorios = Reminder.objects.filter(user=request.user, is_active=True)
    
    # Obtener todos los documentos pendientes
    documentos_pendientes = Documento.objects.filter(reminder__user=request.user, estado='pendiente')
    
    # Crear documentos a partir de recordatorios si no existen
    for recordatorio in recordatorios:
        # Dividir la lista de documentos del recordatorio
        docs_list = [doc.strip() for doc in recordatorio.documents.split('\n') if doc.strip()]
        
        # Crear documentos para cada uno si no existen
        for doc_nombre in docs_list:
            # Verificar si ya existe un documento con este nombre para este recordatorio
            if not Documento.objects.filter(
                reminder=recordatorio, 
                nombre=doc_nombre
            ).exists():
                # Crear nuevo documento con los valores del recordatorio
                Documento.objects.create(
                    reminder=recordatorio,
                    nombre=doc_nombre,
                    tipo=recordatorio.appointment_type,
                    estado='pendiente'
                )
    
    # Obtener todos los documentos pendientes actualizados y ordenarlos por fecha de creación
    documentos = Documento.objects.filter(reminder__user=request.user, estado='pendiente').order_by('-fecha_creacion')
    
    # Filtrar documentos que no tienen nombre o tipo válido
    documentos = documentos.exclude(nombre='Documento sin nombre').exclude(tipo='general')
    
    return render(request, 'vitalia_app/documentos_pendientes.html', {
        'documentos': documentos,
        'recordatorios': recordatorios
    })

@login_required
def confirmar_documento(request, documento_id):
    documento = get_object_or_404(Documento, id=documento_id, reminder__user=request.user)
    
    # Confirmar el documento
    documento.confirmar()
    
    return redirect('vitalia_app:documentos_pendientes')
