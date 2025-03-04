from django import forms
from .models import MedicationReminder

class MedicationReminderForm(forms.ModelForm):
    days_of_week = forms.MultipleChoiceField(
        choices=[
            ('Lunes', 'Lunes'),
            ('Martes', 'Martes'),
            ('Miércoles', 'Miércoles'),
            ('Jueves', 'Jueves'),
            ('Viernes', 'Viernes'),
            ('Sábado', 'Sábado'),
            ('Domingo', 'Domingo'),
        ],
        widget=forms.CheckboxSelectMultiple,
    )

    class Meta:
        model = MedicationReminder
        fields = ['medication_name', 'days_of_week', 'start_date', 'end_date']
