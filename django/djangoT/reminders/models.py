from django.db import models

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

    def __str__(self):
        return f"{self.fecha} {self.hora} - {self.doctor.nombre}"

# Modelo de Recordatorio de Medicación
class MedicationReminder(models.Model):
    medication_name = models.CharField(max_length=100)
    days_of_week = models.CharField(max_length=50)  # Ejemplo: "Lunes, Miércoles, Viernes"
    start_date = models.DateField()
    end_date = models.DateField()

    def __str__(self):
        return self.medication_name

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
