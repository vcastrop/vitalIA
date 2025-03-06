from django.db import models

class Especialidad(models.Model):
    nombre = models.CharField(max_length=100)

    def __str__(self):
        return self.nombre

class Doctor(models.Model):
    nombre = models.CharField(max_length=100)
    especialidad = models.ForeignKey(Especialidad, on_delete=models.CASCADE)

    def __str__(self):
        return self.nombre

class Cita(models.Model):
    fecha = models.DateField()
    hora = models.TimeField()  # Asegúrate de que este campo existe
    especialidad = models.ForeignKey(Especialidad, on_delete=models.CASCADE)
    doctor = models.ForeignKey('Doctor', on_delete=models.CASCADE)
    disponible = models.BooleanField(default=True)

    def __str__(self):
        return f"{self.fecha} {self.hora} - {self.doctor.nombre}"
