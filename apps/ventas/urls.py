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


    path('Usuarios/', listUsuarios, name='listUsuarios'),
    path('nuevo_u/', usuariosCreate, name='usuariosCreate'), 
    path('actualizar_u/<int:id_usuario>/', usuariosEdit, name='usuariosEdit'), 
    path('eliminar_u/<int:id_usuario>/', usuariosEliminar, name='usuariosEliminar'),


    path('consulta1/', consulta1, name='consulta1'),
    path('consulta2/', consulta2, name='consulta2'),
    path('consulta3/', consulta3, name='consulta3'),
    path('consulta4/', consulta4, name='consulta4'),
]