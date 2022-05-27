from django import forms
from apps.ventas.models import Usuario

class UsuarioForm(forms.ModelForm):
    class Meta:
        model = Usuario
   
        fields = [
            'nombres',
            'tipoIdentificacion',
            'num_identificacion',
            'telefono',
            'direccion',
        ]
       
        labels = {
            'nombres': 'Ingrese los nombres',
            'tipoIdentificacion': 'Ingrese el tipo de identificación',
            'num_identificacion': 'Ingrese el número de identificación',
            'telefono': 'Ingrese el número de teléfono',
            'direccion': 'Ingrese la dirección',
        }

        widgets ={
            'nombres': forms.TextInput(attrs={'class': 'form-control'}),
            'tipoIdentificacion': forms.TextInput(attrs={'class': 'form-control'}),
            'num_identificacion': forms.TextInput(attrs={'class': 'form-control'}),
            'telefono': forms.TextInput(attrs={'class': 'form-control'}),
            'direccion': forms.TextInput(attrs={'class': 'form-control'}),
            }