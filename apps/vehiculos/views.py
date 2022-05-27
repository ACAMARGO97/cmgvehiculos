from django.shortcuts import redirect, render
from apps.vehiculos.models import Vehiculos, Marca, Tipovehiculo
from apps.vehiculos.fromVehiculo import VehiculoFrom
from apps.vehiculos.formMarca import MarcaForm
from apps.vehiculos.formTipoVehiculo import TipoVehiculosForm


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


#marca

def listMarcas(request):
    marcas = Marca.objects.all().order_by('-id') 
    context = {'vehiculos':marcas} 
    return render(request, 'marcas/listMarcas.html', context) 

def marcaCreate(request):
    if request.method == 'POST':
        form = MarcaForm(request.POST) 
        if form.is_valid():
            form.save()
        return redirect('vehiculos:listMarcas') 
    else:
        form =MarcaForm()
        return render(request,'marcas/marca_form.html', {'form': form})

def marcaEdit(request, id_marca):
    marca = Marca.objects.get(pk=id_marca)

    if request.method == 'GET':
        form = MarcaForm(instance=marca)
    else:
        form =MarcaForm(request.POST, instance=marca) 
        if form.is_valid():
            form.save()
        return redirect('vehiculos:listMarcas') 

    return render(request,'marcas/marca_form.html', {'form': form})
 
def marcaEliminar(request, id_marca):
    marca = Marca.objects.get(pk=id_marca)

    if request.method == 'POST':
       marca.delete()
       return redirect('vehiculos:listMarcas')
    return render(request,'marcas/marcaEliminar.html', {'marca': marca})  

#Tipovehiculo
def listTipoVehiculo(request):
    tipoVehiculos = Tipovehiculo.objects.all().order_by('-id') 
    context = {'vehiculos':tipoVehiculos} 
    return render(request, 'tipoVehiculos/listTipoVehiculos.html', context) 

def tipoVehiculosCreate(request):
    if request.method == 'POST':
        form = TipoVehiculosForm(request.POST) 
        if form.is_valid():
            form.save()
        return redirect('vehiculos:listTipoVehiculo') 
    else:
        form =TipoVehiculosForm()
        return render(request,'tipoVehiculos/tipoVehiculos_form.html', {'form': form})

def tipoVehiculosEdit(request, id_tipoVehiculo):
    tipoVehiculos = Tipovehiculo.objects.get(pk=id_tipoVehiculo)
    if request.method == 'GET':
        form = TipoVehiculosForm(instance=tipoVehiculos)
    else:
        form =TipoVehiculosForm(request.POST, instance=tipoVehiculos) 
        if form.is_valid():
            form.save()
        return redirect('vehiculos:listTipoVehiculo') 

    return render(request,'tipoVehiculos/tipoVehiculos_form.html', {'form': form})
 
def tipoVehiculosEliminar(request, id_tipoVehiculo):
    tipoVehiculos = Tipovehiculo.objects.get(pk=id_tipoVehiculo)

    if request.method == 'POST':
       tipoVehiculos.delete()
       return redirect('vehiculos:listTipoVehiculo')
    return render(request,'tipoVehiculos/tipoVehiculosEliminar.html', {'tipoVehiculos': tipoVehiculos})  