# reminder_app/models.py
from django.db import models

class Reminder(models.Model):
    appointment_id = models.IntegerField()
    user_email = models.EmailField()
    reminder_time = models.DateTimeField()
    confirmed = models.BooleanField(default=False)

    def __str__(self):
        return f"Reminder for {self.user_email} at {self.reminder_time}"

class DocumentReminder(models.Model):
    reminder = models.OneToOneField(Reminder, on_delete=models.CASCADE)
    required_documents = models.TextField()

    def save(self, *args, **kwargs):
        # Si no se ha definido el mensaje, lo generamos automáticamente
        if not self.required_documents:
            user_name = self.reminder.user_email.split('@')[0].replace(".", " ").capitalize()  # Extrae el nombre de usuario
            self.required_documents = f"Hola {user_name}, recuerda traer los siguientes documentos: cédula, carnet, y cualquier otro documento requerido."
        super(DocumentReminder, self).save(*args, **kwargs)

    def __str__(self):
        return f"Documents for {self.reminder.user_email}: {self.required_documents}"
