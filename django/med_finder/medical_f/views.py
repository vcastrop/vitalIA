from django.shortcuts import render
from rapidfuzz import process
from rapidfuzz.fuzz import WRatio  # Importa WRatio directamente
from med_finder.medical_f.models import Medicamento, StockMedicamento, Farmacia

def homeMedF(request):
    return render(request, 'homeMedF.html')

def buscar_medicamentos(request):
    query = request.GET.get('query', '').strip()  # Quita espacios en blanco

    resultados_finales = []
    sugerencias = []

    if query:  # Solo buscar si hay un término ingresado
        # Buscar coincidencias exactas
        resultados = StockMedicamento.objects.filter(
            medicamento__nombre__icontains=query
        ).select_related('medicamento', 'farmacia')

        # Verificar si el término coincide exactamente con algún medicamento
        existe_medicamento_exacto = Medicamento.objects.filter(nombre__iexact=query).exists()

        if resultados.exists():
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
        elif not existe_medicamento_exacto:
            # Si no hay resultados exactos y no coincide exactamente, buscar coincidencias aproximadas
            nombres_medicamentos = Medicamento.objects.values_list('nombre', flat=True)
            sugerencias = process.extract(query, nombres_medicamentos, limit=3, scorer=WRatio)  # Usa WRatio directamente
            sugerencias = [s[0] for s in sugerencias if s[1] > 70]  # Filtrar por similitud > 70%

    return render(request, 'buscar_medicamentos.html', {
        'query': query,
        'resultados': resultados_finales,
        'sugerencias': sugerencias,
    })