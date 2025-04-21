from django.db import models

from django.contrib.auth.models import User

# Modelo de Recordatorio de Medicación
class MedicationReminder(models.Model):
    medication_name = models.CharField(max_length=100)
    days_of_week = models.CharField(max_length=50)
    start_date = models.DateField()
    end_date = models.DateField()
    usuario = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)  # 🔥 esto es clave
