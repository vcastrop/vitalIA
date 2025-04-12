from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone

class Paciente(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, null=True, blank=True)
    nombre = models.CharField(max_length=200)
    edad = models.IntegerField()
    direccion = models.CharField(max_length=300)
    telefono = models.CharField(max_length=15)
    email = models.EmailField(max_length=200)
    
    def __str__(self):
        return self.nombre



class Documento(models.Model):
    reminder = models.ForeignKey('reminder_app.Reminder', on_delete=models.CASCADE, null=True, blank=True)
    nombre = models.CharField(max_length=255)
    tipo = models.CharField(max_length=50)
    estado = models.CharField(max_length=20, default='pendiente')
    fecha_creacion = models.DateTimeField(default=timezone.now)
    fecha_confirmacion = models.DateTimeField(null=True, blank=True)

    def confirmar(self):
        self.estado = 'confirmado'
        self.fecha_confirmacion = timezone.now()
        self.save()

    def __str__(self):
        return f"{self.nombre} - {self.estado}"

