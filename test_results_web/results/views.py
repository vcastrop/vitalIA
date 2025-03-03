from django.shortcuts import render
from .models import MedicalResult

def result_list(request):
    results = MedicalResult.objects.all().order_by("-date_uploaded")
    return render(request, "results/result_list.html", {"results": results})
