from django.db import models
from django.contrib.auth.models import User

class Reminder(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)
    title = models.CharField(max_length=200, help_text="Título del recordatorio", default="Recordatorio de Documentos")
    appointment_date = models.DateTimeField()
    documents = models.TextField(help_text="Lista de documentos necesarios")
    description = models.TextField(blank=True, help_text="Descripción adicional del recordatorio")
    created_at = models.DateTimeField(auto_now_add=True)
    is_active = models.BooleanField(default=True)
    notification_sent = models.BooleanField(default=False)

    def __str__(self):
        return f"{self.title} - {self.appointment_date.strftime('%d/%m/%Y %H:%M')}"

    class Meta:
        ordering = ['appointment_date']
        verbose_name = 'Recordatorio'
        verbose_name_plural = 'Recordatorios'
