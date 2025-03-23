from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from .models import Reminder
from .forms import ReminderForm

def reminder_dashboard(request):
    return render(request, 'reminder_app/reminder_dashboard.html')

def reminder_list(request):
    reminders = Reminder.objects.filter(is_active=True)
    return render(request, 'reminder_app/reminder_list.html', {'reminders': reminders})

def create_reminder(request):
    if request.method == 'POST':
        form = ReminderForm(request.POST)
        if form.is_valid():
            reminder = form.save()
            messages.success(request, 'Recordatorio creado exitosamente.')
            return redirect('reminder_app:reminder_list')
    else:
        form = ReminderForm()
    return render(request, 'reminder_app/create_reminder.html', {'form': form})

def delete_reminder(request, pk):
    reminder = get_object_or_404(Reminder, pk=pk)
    reminder.is_active = False
    reminder.save()
    messages.success(request, 'Recordatorio eliminado exitosamente.')
    return redirect('reminder_app:reminder_list')
