from django.db import models

class Especialidad(models.Model):
    nombre = models.CharField(max_length=100)

    def __str__(self):
        return self.nombre

class Cita(models.Model):
    fecha = models.DateField()
    hora = models.TimeField()
    especialidad = models.ForeignKey(Especialidad, on_delete=models.CASCADE)
    disponible = models.BooleanField(default=True)  # Para marcar si está ocupada

    def __str__(self):
        return f"{self.fecha} - {self.hora} ({self.especialidad.nombre})"
