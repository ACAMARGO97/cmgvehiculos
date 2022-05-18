from django.urls import path
from apps.vehiculos.views import listVehiculos, vehiculoCreate, vehiculoEdit, vehiculoEliminar

app_name = 'vehiculos'
urlpatterns = [
    path('', listVehiculos, name='listVehiculos'),
    path('nuevo/', vehiculoCreate, name='vehiculoCreate'),
    path('actualizar/<int:id_vehiculos>/', vehiculoEdit, name='vehiculoEdit'),
    path('eliminar/<int:id_vehiculos>/', vehiculoEliminar, name='vehiculoEliminar')
]