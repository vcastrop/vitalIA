from django.db import models
from django.contrib.auth.models import User

# Modelo de Especialidad
class Especialidad(models.Model):
    nombre = models.CharField(max_length=100)

    def __str__(self):
        return self.nombre

# Modelo de Doctor
class Doctor(models.Model):
    nombre = models.CharField(max_length=100)
    especialidad = models.ForeignKey(Especialidad, on_delete=models.CASCADE)

    def __str__(self):
        return self.nombre

# Modelo de Cita Médica
class Cita(models.Model):
    fecha = models.DateField()
    hora = models.TimeField()
    especialidad = models.ForeignKey(Especialidad, on_delete=models.CASCADE)
    doctor = models.ForeignKey(Doctor, on_delete=models.CASCADE)
    disponible = models.BooleanField(default=True)
    usuario = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True)  # 👈 nuevo campo

    def __str__(self):
        return f"{self.fecha} {self.hora} - {self.doctor.nombre}"

