from .forms import MedicationReminderForm
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect, get_object_or_404
from .models import MedicationReminder


def home(request):
    return render(request, 'reminders/homeReminders.html')

@login_required
def add_medication_reminder(request):
    if request.method == "POST":
        form = MedicationReminderForm(request.POST)
        if form.is_valid():
            reminder = form.save(commit=False)
            reminder.usuario = request.user  # 👈 Aquí se asocia al usuario logueado
            reminder.save()
            return redirect('add_reminder')
    else:
        form = MedicationReminderForm()

    # 👇 Solo recordatorios del usuario actual
    reminders = MedicationReminder.objects.filter(usuario=request.user)
    return render(request, 'reminders/add_medication_reminder.html', {'form': form, 'reminders': reminders})

@login_required
def delete_medication_reminder(request, pk):
    reminder = get_object_or_404(MedicationReminder, pk=pk)
    reminder.delete()
    return redirect('add_reminder')
