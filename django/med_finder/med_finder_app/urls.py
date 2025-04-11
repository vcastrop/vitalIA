from django.urls import path
from med_finder.medical_f.views import homeMedF, buscar_medicamentos

urlpatterns = [
    path('', homeMedF, name='homeMedF'),
    path('buscar-medicamentos/', buscar_medicamentos, name='buscar_medicamentos'),
]