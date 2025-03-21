from django import forms

class BuscarMedicamentoForm(forms.Form):
    query = forms.CharField(label="Buscar medicamento", max_length=255, required=False)
