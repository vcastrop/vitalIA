from django.shortcuts import render
import random
from vitalIA_app.models import Medicamento, StockMedicamento, Farmacia

def home(request):
    return render(request, 'home.html')

def buscar_medicamentos(request):
    query = request.GET.get('query', '').strip()  # Quita espacios en blanco

    resultados_finales = []

    if query:  # Solo buscar si hay un término ingresado
        resultados = StockMedicamento.objects.filter(
            medicamento__nombre__icontains=query
        ).select_related('medicamento', 'farmacia')

        # Agrupar resultados por medicamento
        medicamentos = {}
        for stock in resultados:
            if stock.medicamento.nombre not in medicamentos:
                medicamentos[stock.medicamento.nombre] = {
                    "descripcion": stock.medicamento.descripcion,
                    "farmacias": []
                }
            medicamentos[stock.medicamento.nombre]["farmacias"].append({
                "farmacia": stock.farmacia.nombre,
                "precio": stock.precio,
                "stock": stock.stock
            })

        # Convertir a lista de resultados
        resultados_finales = [
            {"medicamento": nombre, **detalles}
            for nombre, detalles in medicamentos.items()
        ]

    return render(request, 'buscar_medicamentos.html', {
        'query': query,
        'resultados': resultados_finales
    })