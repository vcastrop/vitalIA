from django.shortcuts import render, redirect
from .models import MedicationReminder
from .forms import MedicationReminderForm


def home(request):
    return render(request, 'reminders/home.html')


def add_medication_reminder(request):
    if request.method == "POST":
        form = MedicationReminderForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('add_reminder')
    else:
        form = MedicationReminderForm()

    reminders = MedicationReminder.objects.all()
    return render(request, 'reminders/add_medication_reminder.html', {'form': form, 'reminders': reminders})
