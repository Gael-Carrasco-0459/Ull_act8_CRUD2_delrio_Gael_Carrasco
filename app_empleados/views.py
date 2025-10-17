from django.shortcuts import render, redirect, get_object_or_404
from .models import Empleado

# Listar empleados
def index(request):
    empleados = Empleado.objects.all()
    return render(request, 'listar_empleados.html', {'empleado': empleados})

# Ver empleado (opcional, puedes usarlo si quieres detalle)
def ver_empleado(request, id):
    empleado = get_object_or_404(Empleado, id=id)
    return render(request, 'ver_empleado.html', {'empleado': empleado})

# Agregar empleado
def agregar_empleado(request):
    if request.method == 'POST':
        nombre = request.POST['nombre']
        apellidos = request.POST['apellidos']
        puesto = request.POST['puesto']
        salario = request.POST['salario']
        fechingreso = request.POST['fechingreso']
        Empleado.objects.create(nombre=nombre, apellidos=apellidos, puesto=puesto, salario=salario, fechingreso=fechingreso)
        return redirect('inicio')
    return render(request, 'agregar_empleado.html')

# Editar empleado
def editar_empleado(request, id):
    empleado = get_object_or_404(Empleado, id=id)
    if request.method == 'POST':
        empleado.nombre = request.POST['nombre']
        empleado.apellidos = request.POST['apellidos']
        empleado.puesto = request.POST['puesto']
        empleado.salario = request.POST['salario']
        empleado.fechingreso = request.POST['fechingreso']
        empleado.save()
        return redirect('inicio')
    return render(request, 'editar_empleado.html', {'empleado': empleado})

# Borrar empleado
def borrar_empleado(request, id):
    empleado = get_object_or_404(Empleado, id=id)
    if request.method == 'POST':
        empleado.delete()
        return redirect('inicio')
    return render(request, 'borrar_empleado.html', {'empleado': empleado})