from django.core.management.base import BaseCommand
from vitalIA_app.models import Medicamento, Farmacia, StockMedicamento
import random

class Command(BaseCommand):
    help = "Poblar la base de datos con medicamentos y farmacias"

    def handle(self, *args, **kwargs):
        medicamentos_lista = [
            "Ibuprofeno", "Paracetamol", "Amoxicilina", "Omeprazol", "Metformina",
            "Loratadina", "Aspirina", "Losartan", "Salbutamol", "Atorvastatina"
        ]

        farmacias_lista = ["Farmacia A", "Farmacia B", "Farmacia C", "Farmacia D", "Farmacia E"]

        # Crear medicamentos SIN DUPLICADOS
        for nombre in medicamentos_lista:
            Medicamento.objects.get_or_create(
                nombre=nombre.strip().lower(),
                defaults={"descripcion": f"Descripción de {nombre}"}
            )

        # Crear farmacias SIN DUPLICADOS
        for nombre in farmacias_lista:
            Farmacia.objects.get_or_create(nombre=nombre.strip())

        # Poblar relación StockMedicamento
        medicamentos = Medicamento.objects.all()
        farmacias = Farmacia.objects.all()

        for farmacia in farmacias:
            for medicamento in medicamentos:
                precio = random.randint(10000, 50000)  # Precio entre 10,000 y 50,000
                stock = random.randint(10, 100)  # Stock entre 10 y 100
                StockMedicamento.objects.update_or_create(
                    farmacia=farmacia,
                    medicamento=medicamento,
                    defaults={'precio': precio, 'stock': stock}
                )

        self.stdout.write(self.style.SUCCESS("✅ Base de datos poblada exitosamente 🎉"))
