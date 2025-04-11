from django import forms
from .models import Reminder

class ReminderForm(forms.ModelForm):
    class Meta:
        model = Reminder
        fields = ['title', 'appointment_type', 'appointment_date', 'documents']
        widgets = {
            'appointment_date': forms.DateTimeInput(
                attrs={'type': 'datetime-local'},
                format='%Y-%m-%dT%H:%M'
            ),
            'documents': forms.Textarea(
                attrs={'rows': 4, 'placeholder': 'Lista de documentos necesarios'}
            ),
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['title'].widget.attrs.update({
            'class': 'form-control',
            'placeholder': 'Título del recordatorio'
        })
        self.fields['appointment_type'].widget.attrs.update({
            'class': 'form-control'
        })
        self.fields['documents'].widget.attrs.update({
            'class': 'form-control'
        }) 