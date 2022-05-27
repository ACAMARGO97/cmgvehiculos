from django import forms
from apps.ventas.models import Venta

class VentaForm(forms.ModelForm):
    class Meta:
        model = Venta
        fields = [
            'fecha',
            'ValorTotal',
            'tipoPago',
            'user',
        ]

        labels = {
            'fecha': 'Ingresar el fecha',
            'ValorTotal': 'Ingresar el valor total',
            'tipoPago': 'Ingresar el tipo de pago',
            'user': 'Ingresar el usuario',
        }

        Widgets = {
            'fecha': forms.TextInput(attrs={'class': 'form-control'}),
            'ValorTotal': forms.TextInput(attrs={'class': 'form-control'}),
            'tipoPago': forms.TextInput(attrs={'class': 'form-control'}),
            'user': forms.Select(attrs={'class': 'form-control'}),
        }