from django.db import models
from django.contrib.auth.models import User

# Modelo de Resultados Médicos
class MedicalResult(models.Model):
    name = models.CharField(max_length=255)  # Nombre del documento
    description = models.TextField(blank=True, null=True)  # Descripción opcional
    file = models.FileField(upload_to="medical_results/")  # Archivo subido
    date_uploaded = models.DateTimeField(auto_now_add=True)  # Fecha de subida
    result_type = models.CharField(max_length=100, choices=[
        ("blood_test", "Análisis de sangre"),
        ("x_ray", "Radiografía"),
        ("mri", "Resonancia magnética"),
        ("other", "Otro")
    ])

    def __str__(self):
        return f"{self.name} ({self.result_type})"
