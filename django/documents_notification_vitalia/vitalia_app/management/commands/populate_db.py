# vitalia_app/management/commands/populate_db.py
from django.core.management.base import BaseCommand
from vitalia_app.models import Paciente, Documento

class Command(BaseCommand):
    help = 'Puebla la base de datos con pacientes y sus documentos'

    def handle(self, *args, **kwargs):
        pacientes_data = [
            {
                'nombre': 'Juan Pérez',
                'edad': 30,
                'email': 'juan.perez@example.com',
                'telefono': '3214567890',
                'documentos': ['Cédula de ciudadanía', 'Historia clínica'],
            },
            {
                'nombre': 'Ana Gómez',
                'edad': 25,
                'email': 'ana.gomez@example.com',
                'telefono': '3123456789',
                'documentos': ['Cédula de ciudadanía', 'Examen de sangre'],
            },
            {
                'nombre': 'Carlos Ruiz',
                'edad': 45,
                'email': 'carlos.ruiz@example.com',
                'telefono': '3112345678',
                'documentos': ['Cédula de ciudadanía', 'Radiografía'],
            },
            {
                'nombre': 'Luisa Martínez',
                'edad': 35,
                'email': 'luisa.martinez@example.com',
                'telefono': '3101234567',
                'documentos': ['Cédula de ciudadanía', 'ECG'],
            },
            {
                'nombre': 'Pedro López',
                'edad': 50,
                'email': 'pedro.lopez@example.com',
                'telefono': '3198765432',
                'documentos': ['Cédula de ciudadanía', 'Examen de orina'],
            },
            {
                'nombre': 'María Fernández',
                'edad': 60,
                'email': 'maria.fernandez@example.com',
                'telefono': '3187654321',
                'documentos': ['Cédula de ciudadanía', 'Tomografía'],
            },
            {
                'nombre': 'Jorge Sánchez',
                'edad': 40,
                'email': 'jorge.sanchez@example.com',
                'telefono': '3176543210',
                'documentos': ['Cédula de ciudadanía', 'Consulta médica'],
            },
            {
                'nombre': 'Sandra Morales',
                'edad': 29,
                'email': 'sandra.morales@example.com',
                'telefono': '3165432109',
                'documentos': ['Cédula de ciudadanía', 'Análisis de sangre'],
            },
            {
                'nombre': 'David Rodríguez',
                'edad': 38,
                'email': 'david.rodriguez@example.com',
                'telefono': '3154321098',
                'documentos': ['Cédula de ciudadanía', 'Examen de presión'],
            },
            {
                'nombre': 'Carmen Díaz',
                'edad': 28,
                'email': 'carmen.diaz@example.com',
                'telefono': '3143210987',
                'documentos': ['Cédula de ciudadanía', 'Resultados de laboratorio'],
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
