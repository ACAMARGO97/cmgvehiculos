from django import forms
from apps.vehiculos.models import Tipovehiculo

class TipoVehiculosForm(forms.ModelForm):
    class Meta:
        model = Tipovehiculo
    
        fields = [
            'nombre',
        ]
 
        labels = {
            'nombre': 'Ingrese el nombre',
        }

        widgets ={
            'nombre': forms.TextInput(attrs={'class': 'form-control'}), 
        }