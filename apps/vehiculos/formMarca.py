from django import forms
from apps.vehiculos.models import Marca

class MarcaForm(forms.ModelForm):
    class Meta:
        model = Marca
    
        fields = [
            'nombre',
        ]
 
        labels = {
            'nombre': 'Ingrese el nombre',
        }

        widgets ={
            'nombre': forms.TextInput(attrs={'class': 'form-control'}),
        }
