# urls.py
from django.urls import path
from . import views

app_name = 'vitalia_app'

urlpatterns = [
    path('', views.inicio, name='inicio'),  
    path('ver-pacientes/', views.ver_pacientes, name='ver_pacientes'),
    path('confirmar-documentos/', views.confirmar_documentos, name='confirmar_documentos'),
    path('confirmar-documento/<int:documento_id>/', views.confirmar_documento, name='confirmar_documento'),
]
