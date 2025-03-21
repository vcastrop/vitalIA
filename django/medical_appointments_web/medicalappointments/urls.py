from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('appointments/', include('medical_appointments_web.appointments.urls')),  # Solo dejamos esta
]
