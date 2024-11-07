from django.shortcuts import render
from .servicios import solicitar
from .servicios import solicitar2
from .servicios import solicitudP
from .models import Archivos,Planetas
from .forms import FormArchivos,FormPlanetas
from django.contrib import messages

# Create your views here.
def principal(request):
    return render(request, 'ejercicios/principal.html',{'datos':solicitar})


def mensajes(request):
    return render(request, 'ejercicios/mensajes.html',{'mensajes':solicitar2})


def planetas(request):
    resultado = solicitudP()
    if request.method == 'POST':
        form = FormPlanetas(request.POST, request.FILES)
        
        if form.is_valid():
            archivo = request.FILES.get('archivo')
            planeta = Planetas(
                name=resultado.get('name'),
                rotation_period=resultado.get('rotation_period'),
                orbital_period=resultado.get('orbital_period'),
                climate=resultado.get('climate'),
                terrain=resultado.get('terrain'),
                archivo=archivo
            )
            planeta.save()
            
            messages.success(request, "Datos del planeta guardados correctamente.")
            return render(request, "ejercicios/planetas.html", {'resultados': [resultado], 'form': form})
        
        else:
            messages.error(request, "Error al procesar el formulario.")
    
    else:
        form = FormPlanetas() 
    
    return render(request, "ejercicios/planetas.html", {'resultados': [resultado], 'form': form})


def archivos(request):
    if request.method=='POST':
        form = FormArchivos(request.POST, request.FILES)
        if form.is_valid():
            titulo=request.POST['titulo']
            descripcion=request.POST['descripcion']
            archivo = request.FILES.get('archivo')
            insert = Archivos(titulo=titulo,descripcion=descripcion,archivo=archivo)
            insert.save()
            return render(request, "ejercicios/archivos.html")
        
        else:
            messages.error(request, "Error al procesar formulario")

    else:
        return render(request,"ejercicios/archivos.html",{'archivo':Archivos})

# def planetas(request):
#      resultado = solicitudP()
#      resultados = [resultado] if resultado else []
#      return render(request, 'ejercicios/planetas.html', {'resultados': resultados})