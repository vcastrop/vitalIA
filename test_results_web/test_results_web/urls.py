from django.contrib import admin
from django.urls import path, include
from django.shortcuts import redirect

def home_redirect(request):
    return redirect("result_list")  # Redirige la raíz a la vista de resultados

urlpatterns = [
    path("", home_redirect),  # Redirige la raíz (/) a "results/"
    path("admin/", admin.site.urls),
    path("results/", include("results.urls")),
]
