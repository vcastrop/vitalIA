from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('add/', views.add_medication_reminder, name='add_medication_reminder'),
    path('add/save', views.add_medication_reminder, name='add_reminder'),
    path('delete/<int:pk>/', views.delete_medication_reminder, name='delete_reminder'),
]
