from django.urls import path
from . import views

app_name = 'reminder_app'

urlpatterns = [
    path('', views.reminder_dashboard, name='reminder_dashboard'),  # Cambiado de home a reminder_dashboard
    path('list/', views.reminder_list, name='reminder_list'),
    path('create/', views.create_reminder, name='create_reminder'),
    path('delete/<int:pk>/', views.delete_reminder, name='delete_reminder'),
    path('suggest-documents/', views.suggest_documents, name='suggest_documents'),
]
