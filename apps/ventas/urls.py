from django.urls import path
from apps.ventas.views import *

app_name='ventas'
urlpatterns = [
    path('', listVentas, name='listVentas'),
    path('nuevo/', ventaCreate, name='ventaCreate'),
    path('actualizar/<int:id_venta>/', ventaEdit, name='ventaEdit'), 
    path('eliminar/<int:id_venta>/', ventaElim, name='ventaElim'), 

    path('VehiculoVenta/', listVehiculoVentas, name='listVehiculoVentas'),
    path('nuevo_vv/', vehiculoVentasCreate, name='vehiculoVentasCreate'), 
    path('actualizar_vv/<int:id_vehiculoVenta>/', vehiculoVentasEdit, name='vehiculoVentasEdit'), 
    path('eliminar_vv/<int:id_vehiculoVenta>/', vehiculoVentasEliminar, name='vehiculoVentasEliminar'), 

]