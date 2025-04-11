from django.db import models

class Paciente(models.Model):
    nombre = models.CharField(max_length=200)
    edad = models.IntegerField()
    direccion = models.CharField(max_length=300)
    telefono = models.CharField(max_length=15)
    email = models.EmailField(max_length=200)
    
    def __str__(self):
        return self.nombre



class Documento(models.Model):
    paciente = models.ForeignKey(Paciente, on_delete=models.CASCADE)
    tipo = models.CharField(max_length=100)
    estado = models.CharField(max_length=50)  # Pendiente o Confirmado

    def __str__(self):
        return f'{self.tipo} de {self.paciente.nombre}'

