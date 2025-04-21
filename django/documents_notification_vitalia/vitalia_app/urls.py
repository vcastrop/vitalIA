# urls.py
from django.urls import path
from . import views

app_name = 'vitalia_app'

urlpatterns = [
    path('', views.inicio, name='inicio'),  
    path('documentos-pendientes/', views.confirmar_documentos, name='documentos_pendientes'),
    path('documentos-confirmados/', views.ver_documentos_confirmados, name='documentos_confirmados'),
    path('confirmar-documento/<int:documento_id>/', views.confirmar_documento, name='confirmar_documento'),
]
