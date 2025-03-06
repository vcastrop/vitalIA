from django.contrib import admin
from .models import Cita

@admin.register(Cita)
class CitaAdmin(admin.ModelAdmin):
    list_display = ("fecha", "hora", "especialidad", "disponible")
    list_filter = ("especialidad", "disponible")
