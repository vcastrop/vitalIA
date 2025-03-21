from django.shortcuts import render
from .models import Reminder

def reminder(request):
    reminders = Reminder.objects.all().order_by('-reminder_time')  # Ordenado por fecha del recordatorio
    return render(request, 'reminder_app/reminder_list.html', {'reminders': reminders})
