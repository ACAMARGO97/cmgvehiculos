from django import forms
from apps.ventas.models import VehiculoVenta

class VehiculoVentaForm(forms.ModelForm):
    class Meta:
        model = VehiculoVenta
        fields = [
            'vehiculo',
            'venta',
            'cantidad',
            'precio',
        ]
        labels = {
            'vehiculo':'Elija el modelo del vehiculo',
            'venta': 'Elija el id de la venta',
            'cantidad': 'Ingrese la cantidad',
            'precio': 'Ingrese el precio',
        }

        widgets ={
            'cantidad': forms.DateInput(attrs={'class': 'form-control'}),
            'precio': forms.TextInput(attrs={'class': 'form-control'}),
            'tipoPago': forms.TextInput(attrs={'class': 'form-control'}),
            'vehiculo': forms.Select(attrs={'class': 'form-control'}),
            'venta': forms.Select(attrs={'class': 'form-control'}),
        }