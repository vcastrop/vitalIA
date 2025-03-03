from django.db import models


# Create your models here.

class appointments(models.Model):
    especialidad = models.CharField(max_length=100)
    fecha = models.DateField()
    hora = models.TimeField()
    disponible = models.BooleanField(default=True)

    def __str__(self):
        return f"{self.especialidad} - {self.fecha} {self.hora}"