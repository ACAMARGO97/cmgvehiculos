from django import forms
from apps.vehiculos.models import Vehiculos

class VehiculoFrom(forms.ModelForm):
    class Meta:
        model = Vehiculos
        fields = [
            'modelo',
            'color',
            'placa',
            'motor',
            'marca',
            'tipovehiculo',
        ]

        labels = {
            'modelo': 'Ingresar el modelo',
            'color': 'Ingresar el color',
            'placa': 'Ingresar la placa',
            'motor': 'Ingresar el motor',
            'marca': 'Ingresar la marca',
            'tipovehiculo': 'Ingresar el tipo de vehiculo',
        }

        Widgets = {
            'modelo': forms.TextInput(attrs={'class': 'form-control'}),
            'color': forms.TextInput(attrs={'class': 'form-control'}),
            'placa': forms.TextInput(attrs={'class': 'form-control'}),
            'motor': forms.TextInput(attrs={'class': 'form-control'}),
            'marca': forms.Select(attrs={'class': 'form-control'}),
            'tipovehiculo': forms.Select(attrs={'class': 'form-control'}),
        }