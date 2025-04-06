# Generated by Django 5.1.7 on 2025-04-01 19:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('reminder_app', '0003_reminder_appointment_type'),
    ]

    operations = [
        migrations.AlterField(
            model_name='reminder',
            name='appointment_type',
            field=models.CharField(choices=[('consulta_general', 'Consulta General'), ('consulta_especialista', 'Consulta con Especialista'), ('analisis_clinico', 'Análisis Clínico'), ('vacunacion', 'Vacunación'), ('otros', 'Otros')], default='otros', max_length=50),
        ),
    ]
