from django.shortcuts import redirect, render
from apps.ventas.models import VehiculoVenta, Venta, Usuario
from apps.ventas.formVenta import VentaForm
from apps.ventas.formVehiculoVenta import VehiculoVentaForm
from apps.ventas.formUsuario import UsuarioForm
from django.db.models import Sum

def listVentas(request):
    ventas = Venta.objects.all().order_by('id') 
    context = {'ventas':ventas} 
    return render(request, 'ventas/listVentas.html', context) 

def home (request):
    return render(request, 'base/base.html')

def ventaCreate(request):
    if request.method == 'POST':
        form = VentaForm(request.POST) 
        if form.is_valid():
            form.save()
        return redirect('ventas:listVentas') 
    else:
        form =VentaForm()
        return render(request,'ventas/venta_form.html', {'form': form})

def ventaEdit(request, id_venta):

    venta= Venta.objects.get(pk=id_venta)

    if request.method == 'GET':
        form = VentaForm(instance=venta) 
    else:
        form =VentaForm(request.POST, instance=venta)
        if form.is_valid():
            form.save()
        
        return redirect('ventas:listVentas')

    return render(request,'ventas/venta_form.html', {'form': form})

def ventaElim(request, id_venta):

    venta= Venta.objects.get(pk=id_venta)

    if request.method == 'POST':
        venta.delete() 
        return redirect('ventas:listVentas')
    
    return render(request,'ventas/ventaEliminar.html', {'ventas': venta})


#VehiculoVenta
def listVehiculoVentas(request):
    vehiculoVentas = VehiculoVenta.objects.all().order_by('-id') 
    context = {'ventas':vehiculoVentas} 
    return render(request, 'vehiculoVentas/listVehiculoVentas.html', context) 


def vehiculoVentasCreate(request):
    if request.method == 'POST':
        form = VehiculoVentaForm(request.POST) 
        if form.is_valid():
            form.save()
        return redirect('ventas:listVehiculoVentas')
    else:
        form =VehiculoVentaForm()
        return render(request,'vehiculoVentas/vehiculoVentas_form.html', {'form': form})

def vehiculoVentasEdit(request, id_vehiculoVenta):
    vehiculoVentas = VehiculoVenta.objects.get(pk=id_vehiculoVenta)

    if request.method == 'GET':
        form = VehiculoVentaForm(instance=vehiculoVentas)
    else:
        form =VehiculoVentaForm(request.POST, instance=vehiculoVentas) 
        if form.is_valid():
            form.save()
        return redirect('ventas:listVehiculoVentas') 

    return render(request,'vehiculoVentas/vehiculoVentas_form.html', {'form': form})
 
def vehiculoVentasEliminar(request, id_vehiculoVenta):
    vehiculoVentas = VehiculoVenta.objects.get(pk=id_vehiculoVenta)

    if request.method == 'POST':
       vehiculoVentas.delete()
       return redirect('ventas:listVehiculoVentas')
    return render(request,'vehiculoVentas/vehiculoVentasEliminar.html', {'vehiculoVentas': vehiculoVentas})



#usuarios
def listUsuarios(request):
    usuarios = Usuario.objects.all().order_by('-id') 
    context = {'ventas':usuarios} 
    return render(request, 'usuarios/listUsuarios.html', context) 


def usuariosCreate(request):
    if request.method == 'POST':
        form = UsuarioForm(request.POST) 
        if form.is_valid():
            form.save()
        return redirect('ventas:listUsuarios')
    else:
        form =UsuarioForm()
        return render(request,'usuarios/usuario_form.html', {'form': form})

def usuariosEdit(request, id_usuario):
    usuario = Usuario.objects.get(pk=id_usuario)

    if request.method == 'GET':
        form = UsuarioForm(instance=usuario)
    else:
        form =UsuarioForm(request.POST, instance=usuario) 
        if form.is_valid():
            form.save()
        return redirect('ventas:listUsuarios') 

    return render(request,'usuarios/usuario_form.html', {'form': form})
 
def usuariosEliminar(request, id_usuario):
    usuario = Usuario.objects.get(pk=id_usuario)

    if request.method == 'POST':
       usuario.delete()
       return redirect('ventas:listUsuarios')
    return render(request,'usuarios/usuarioEliminar.html', {'usuarios': usuario})

#consultas
def consulta1(request):
    fecha1 = request.POST.get('fecha1')
    fecha2 = request.POST.get('fecha2')
    consulta1=Venta.objects.filter(fecha__range=[fecha1,fecha2]).aggregate(Sum('ValorTotal'))
    
    context = {
        'fecha1': fecha1,
        'fecha2': fecha2,
        'consulta1': consulta1,
    }
    print(consulta1)
    return render(request,'consultas/consulta1.html',{'context':context})
          
    
def consulta2(request):
    fecha1 = request.POST.get('fecha1')
    fecha2 = request.POST.get('fecha2')
  
    consulta2=Venta.objects.values('fecha').filter(fecha__range=[fecha1,fecha2]).annotate(total=Sum('ValorTotal'))
    
    return render(request,'consultas/consulta2.html',{'consulta2':consulta2})

def consulta3(request):
    fecha1 = request.POST.get('fecha1')
    fecha2 = request.POST.get('fecha2')
  
    consulta3=Venta.objects.values('tipoPago').filter(fecha__range=[fecha1,fecha2]).annotate(total=Sum('ValorTotal'))
    
    return render(request,'consultas/consulta3.html',{'consulta3':consulta3})

def consulta4(request):
    fecha1 = request.POST.get('fecha1')
    fecha2 = request.POST.get('fecha2')
  
    consulta4=Venta.objects.values('user__nombres').filter(fecha__range=[fecha1,fecha2]).annotate(total=Sum('ValorTotal'))
    return render(request,'consultas/consulta4.html',{'consulta4':consulta4})