# vitalia_app/management/commands/populate_db.py
from django.core.management.base import BaseCommand
from vitalia_app.models import Paciente, Documento

class Command(BaseCommand):
    help = 'Puebla la base de datos con pacientes y sus documentos'

    def handle(self, *args, **kwargs):
        pacientes_data = [
            {
                'nombre': 'Kevin Pabón',
                'edad': 30,
                'email': 'Kevinpabon.perez@example.com',
                'telefono': '3214567890',
                'documentos': ['Cédula de ciudadanía', 'Historia clínica', 'Tomografía', "examen de sangre"],
            },
        ]

        # Insertamos los pacientes y sus documentos
        for paciente_data in pacientes_data:
            paciente = Paciente.objects.create(
                nombre=paciente_data['nombre'],
                edad=paciente_data['edad'],
                email=paciente_data['email'],
                telefono=paciente_data['telefono'],
            )

            # Insertamos los documentos relacionados
            for documento in paciente_data['documentos']:
                Documento.objects.create(
                    paciente=paciente,
                    tipo=documento,  # Aquí se usa "tipo" en lugar de "nombre_documento"
                )

        self.stdout.write(self.style.SUCCESS('Base de datos poblada con éxito!'))
        
    

