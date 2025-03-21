# vitalia_app/admin.py
from django.contrib import admin
from .models import Paciente, Documento

admin.site.register(Paciente)
admin.site.register(Documento)
