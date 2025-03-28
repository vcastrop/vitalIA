from django.contrib import admin
from django.urls import path, include
from django.shortcuts import redirect
from test_results_web.results import views

urlpatterns = [
    path('', lambda request: redirect('/menu/')),
    path('admin/', admin.site.urls),
    path('menu/', views.menu, name="menu"),  # Llamar directamente la vista
    path('appointments/', include('medical_appointments_web.appointments.urls')),  # Incluir las rutas de la app appointments
    path("testresults/", include('test_results_web.results.urls')),  # Integrar test_results_web
    path("medication-management/", include('djangoT.reminders.urls')),
    path("medication-finder/", include('med_finder.med_finder_app.urls')),
    path("document-notification/", include('documents_notification_vitalia.documents_N.urls')),
]
