from django.db import models


# Create your models here.

class Cita(models.Model):
    nombre_paciente = models.CharField(max_length=100)
    especialidad = models.CharField(max_length=100)
    fecha = models.DateField()
    hora = models.TimeField()

    def __str__(self):
        return f"{self.nombre_paciente} - {self.especialidad} ({self.fecha} {self.hora})"