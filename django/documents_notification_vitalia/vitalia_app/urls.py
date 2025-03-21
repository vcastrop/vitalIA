# urls.py
from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),  # Ruta de la página de inicio, que va a la vista 'home'
    path('view_patients/', views.ver_pacientes, name='view_patients'),  # Ruta para ver la lista de pacientes
    path('confirmar_documentos/', views.confirmar_documentos, name='confirmar_documentos'),  # Ruta para confirmar documentos
    path('confirmar_documento/<int:documento_id>/', views.confirmar_documento, name='confirmar_documento'),  # Ruta para confirmar un documento en particular
]
