from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path("admin/", admin.site.urls),
    path('', include('documents_notification_vitalia.vitalia_app.urls')),
    
]
