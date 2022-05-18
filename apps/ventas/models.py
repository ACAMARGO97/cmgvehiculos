from django.db import models
from django.contrib.auth.models import User

from apps import vehiculos
from apps.vehiculos.models import Vehiculos

# Create your models here.


class Venta(models.Model):
    fecha = models.DateField()
    valorTotal = models.BigIntegerField()
    tipoPagp = models.CharField(max_length=20)
    user = models.ForeignKey(User, null=True, blank=True, on_delete=models.CASCADE)
    vehiculos= models.ManyToManyField(Vehiculos, through='VehiculoVenta')


class VehiculoVenta(models.Model):
    vehiculos= models.ForeignKey(Vehiculos, blank=False, null=False, on_delete=models.CASCADE)
    venta= models.ForeignKey(Venta, blank=False, null=False, on_delete=models.CASCADE)
    cantidad= models.IntegerField()
    precio= models.BigIntegerField()
