from django.urls import path
from apps.vehiculos.views import *

app_name = 'vehiculos'
urlpatterns = [
    path('', listVehiculos, name='listVehiculos'),
    path('nuevo/', vehiculoCreate, name='vehiculoCreate'),
    path('actualizar/<int:id_vehiculos>/', vehiculoEdit, name='vehiculoEdit'),
    path('eliminar/<int:id_vehiculos>/', vehiculoEliminar, name='vehiculoEliminar'),


    path('marca/', listMarcas, name='listMarcas'),
    path('nuevo_m/', marcaCreate, name='marcaCreate'), 
    path('actualizar_m/<int:id_marca>/', marcaEdit, name='marcaEdit'), 
    path('eliminar_m/<int:id_marca>/', marcaEliminar, name='marcaEliminar'), 

    
    path('tipoVehiculos/', listTipoVehiculo, name='listTipoVehiculo'),
    path('nuevo_t/', tipoVehiculosCreate, name='tipoVehiculosCreate'), 
    path('actualizar_t/<int:id_tipoVehiculo>/', tipoVehiculosEdit, name='tipoVehiculosEdit'), 
    path('eliminar_t/<int:id_tipoVehiculo>/', tipoVehiculosEliminar, name='tipoVehiculosEliminar'), 
]