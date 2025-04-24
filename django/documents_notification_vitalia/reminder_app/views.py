from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from .models import Reminder
from .forms import ReminderForm
from .ai_handler import ReminderAI
from django.http import JsonResponse
from django.contrib.auth.decorators import login_required


# Inicializar el manejador de IA
ai_handler = ReminderAI()

def reminder_dashboard(request):
    return render(request, 'reminder_app/reminder_dashboard.html')

@login_required
def reminder_list(request):
    reminders = Reminder.objects.filter(user=request.user, is_active=True).order_by('appointment_date')
    return render(request, 'reminder_app/reminder_list.html', {'reminders': reminders})

@login_required
def create_reminder(request):
    if request.method == 'POST':
        form = ReminderForm(request.POST)
        if form.is_valid():
            reminder = form.save(commit=False)
            reminder.user = request.user
            
            # Usar IA para generar la descripción
            reminder.description = ai_handler.generate_reminder_description(
                reminder.title,
                reminder.appointment_type,
                reminder.documents
            )
            
            reminder.save()
            messages.success(request, 'Recordatorio creado exitosamente.')
            return redirect('reminder_app:reminder_list')
    else:
        form = ReminderForm()
    
    return render(request, 'reminder_app/create_reminder.html', {'form': form})

@login_required
def delete_reminder(request, pk):
    try:
        reminder = get_object_or_404(Reminder, pk=pk, user=request.user)
        reminder.delete()
        messages.success(request, 'Recordatorio eliminado exitosamente.')
    except Reminder.DoesNotExist:
        messages.error(request, 'El recordatorio no existe.')
    
    return redirect('reminder_app:reminder_list')

def suggest_documents(request):
    if request.method == 'GET':
        appointment_type = request.GET.get('appointment_type')
        if appointment_type:
            ai_handler = ReminderAI()
            suggested_documents = ai_handler.suggest_documents(appointment_type)
            return JsonResponse({'documents': suggested_documents})
    return JsonResponse({'error': 'Invalid request'}, status=400)
