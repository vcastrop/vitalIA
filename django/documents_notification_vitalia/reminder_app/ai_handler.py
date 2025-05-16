try:
    from transformers import pipeline
    import torch

    _torch_available = True
except ImportError:
    _torch_available = False
    print("⚠️ PyTorch no está disponible. La IA de recordatorios estará deshabilitada.")


class ReminderAI:
    def __init__(self):
        if _torch_available:
            self.generator = pipeline('text-generation', model='gpt2')
        else:
            self.generator = None

    def generate_reminder_description(self, title, appointment_type, documents):
        """Genera una descripción amigable para el recordatorio."""
        base_description = f"¡Hola! Te recuerdo que tienes programado: {title}\n\n"

        type_descriptions = {
            'consulta_general': "🏥 Es hora de tu consulta médica general. Tu salud es importante, así que no olvides llevar todos los documentos necesarios.",
            'consulta_especialista': "👨‍⚕️ Tienes una cita con el especialista. Recuerda que es importante llevar tu historial médico completo para una mejor atención.",
            'analisis_clinico': "🔬 Tienes programados análisis clínicos. Recuerda seguir las instrucciones previas (como el ayuno si es necesario).",
            'vacunacion': "💉 Es momento de tu vacunación. ¡Mantener tus vacunas al día es cuidar tu salud!",
            'otros': "📅 Tienes una cita médica programada. No olvides llevar todos los documentos necesarios."
        }

        description = base_description + type_descriptions.get(appointment_type, type_descriptions['otros'])

        if documents:
            docs_list = [doc for doc in documents.split('\n') if doc]
            if docs_list:
                description += "\n\n📋 Documentos que necesitas llevar:\n"
                for doc in docs_list:
                    description += f"✅ {doc}\n"
                description += "\n💡 Recuerda: Llevar todos los documentos necesarios te ayudará a tener una atención más eficiente."

        description += "\n\n¡Tu salud es nuestra prioridad! Si necesitas hacer algún cambio, no dudes en modificar este recordatorio."

        return description

    def suggest_documents(self, appointment_type):
        """Sugiere documentos basados en el tipo de cita."""
        document_suggestions = {
            'consulta_general': [
                "Documento de identidad",
                "Tarjeta del seguro médico",
                "Historial médico reciente",
                "Lista de medicamentos actuales",
                "Carnet de vacunación"
            ],
            'consulta_especialista': [
                "Documento de identidad",
                "Tarjeta del seguro médico",
                "Historial médico completo",
                "Resultados de exámenes previos",
                "Referencia médica",
                "Lista de medicamentos actuales",
                "Informes médicos relacionados"
            ],
            'analisis_clinico': [
                "Documento de identidad",
                "Tarjeta del seguro médico",
                "Orden médica para análisis",
                "Ayuno (si es requerido)",
                "Lista de medicamentos actuales",
                "Historial médico reciente"
            ],
            'vacunacion': [
                "Documento de identidad",
                "Tarjeta del seguro médico",
                "Cartilla de vacunación",
                "Historial de alergias",
                "Informe médico reciente",
                "Lista de medicamentos actuales"
            ],
            'otros': [
                "Documento de identidad",
                "Tarjeta del seguro médico",
                "Historial médico reciente",
                "Lista de medicamentos actuales"
            ]
        }

        return document_suggestions.get(appointment_type, document_suggestions['otros'])
