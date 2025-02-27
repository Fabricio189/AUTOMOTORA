from django.shortcuts import render, redirect
from .models import Marca, Automovil
from django.contrib import messages
from tkinter import *

# Create your views here.

def  home(request):
    return render(request, 'core/home.html')

def galeria(request):
    return render(request, 'core/galeria.html')

def formulario(request):

    marcas = Marca.objects.all()
    variables = {
        'marcas':marcas
    }

    if request.POST:
        auto = Automovil()
        auto.Patente = request.POST.get('txtPatente')
        auto.Modelo = request.POST.get('txtModelo')
        #auto.Color = request.POST.get('txtColor')
        auto.Anio = request.POST.get('txtAnio')
        marca = Marca()
        marca.id = request.POST.get('cboMarca')
        auto.Marca = marca

        try:
            auto.save()
            variables['mensaje'] = 'Guardado Correctamente'
        except:       
            variables['mensaje'] = 'No se puede Guardar correctamente'     
        
    return render(request, 'core/formulario.html', variables)
    
   
# CRUD DE AUTOMOVIL    
def listar_automoviles(request):

    autos = Automovil.objects.all()

    return render(request, 'core/listar_automoviles.html', {
        'autos':autos
    })

def eliminar_automovil(request, id):
    #buscar el automovil que queremos eliminar
    auto = Automovil.objects.get(id=id)

    try:
        auto.delete()
        mensaje = "Eliminado Correctamente"
        messages.success(request, mensaje)
    except: 
        mensaje = "No se ha podido eliminar"
        messages.error(request, mensaje)

    return redirect('listado_automoviles')

def modificar_automovil(request, id):
   # buscamos el automovil para que el usuario lo pueda modificar
   auto = Automovil.objects.get(id = id) 
   marcas = Marca.objects.all()
   variables = {
       'auto': auto,
       'marcas': marcas
   }

   if request.POST:
        auto = Automovil()
        auto.id = request.POST.get('txtId') 
        auto.Patente = request.POST.get('txtPatente')
        auto.Modelo = request.POST.get('txtModelo')
        #auto.Color = request.POST.get('txtColor')
        auto.Anio = request.POST.get('txtAnio')
        marca = Marca()
        marca.id = request.POST.get('cboMarca')
        auto.Marca = marca

        try:
            auto.save()
            messages.success(request,  'Modificado Correctamente')
        except:       
            messages.error(request, 'No se puede Modificar')
        return redirect('listado_automoviles') # Permite retornar

   return render(request, 'core/modificar_automovil.html', variables)

    
