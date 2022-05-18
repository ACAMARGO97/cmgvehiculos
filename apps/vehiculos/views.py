from django.shortcuts import redirect, render
from apps.vehiculos.models import Vehiculos
from apps.vehiculos.fromVehiculo import VehiculoFrom


def listVehiculos(request):
    vehiculos = Vehiculos.objects.all().order_by('-id')
    context = {'vehiculos':vehiculos}
    return render(request, 'vehiculos/listVehiculos.html', context)

def home (request):
    return render(request, 'base/base.html')

def vehiculoCreate(request):
    if request.method == 'POST':
        form = VehiculoFrom(request.POST)
        if form.is_valid():
            form.save()
        return redirect('vehiculos:listVehiculos')
    else:
        form = VehiculoFrom()
        return render(request, 'vehiculos/vehiculo_form.html', {'form': form})

def vehiculoEdit(request, id_vehiculos):
    vehiculo = Vehiculos.objects.get(pk=id_vehiculos)

    if request.method == 'GET':
        form = VehiculoFrom(instance=vehiculo)
    else:
        form = VehiculoFrom(request.POST, instance=vehiculo)
        if form.is_valid():
            form.save()
        return redirect('vehiculos:listVehiculos')
    
    return render(request, 'vehiculos/vehiculo_form.html', {'form': form})

def vehiculoEliminar(request, id_vehiculos):
    vehiculo = Vehiculos.objects.get(pk=id_vehiculos)

    if request.method == 'POST':
        vehiculo.delete()
        return redirect('vehiculos:listVehiculos')
    return render(request,'vehiculos/vehiculoEliminar.html', {'vehiculo': vehiculo})