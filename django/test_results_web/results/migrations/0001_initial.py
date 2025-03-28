# Generated by Django 5.1.6 on 2025-03-03 01:55

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='MedicalResult',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('description', models.TextField(blank=True, null=True)),
                ('file', models.FileField(upload_to='medical_results/')),
                ('date_uploaded', models.DateTimeField(auto_now_add=True)),
                ('result_type', models.CharField(choices=[('blood_test', 'Análisis de sangre'), ('x_ray', 'Radiografía'), ('mri', 'Resonancia magnética'), ('other', 'Otro')], max_length=100)),
            ],
        ),
    ]
