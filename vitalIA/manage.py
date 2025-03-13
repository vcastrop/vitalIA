#!/usr/bin/env python
import os
import sys

def main():
    """Punto de entrada principal para la gestión del proyecto Django."""
    os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'vitalIA.settings')
    try:
        from django.core.management import execute_from_command_line
    except ImportError as exc:
        raise ImportError(
            "No se pudo importar Django. Asegúrate de que está instalado y "
            "de que tu entorno virtual está activado."
        ) from exc
    execute_from_command_line(sys.argv)

if __name__ == '__main__':
    main()
