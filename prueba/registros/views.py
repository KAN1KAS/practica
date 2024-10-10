from django.shortcuts import render
from .models import Alumnos 
from .forms import ComentarioContactoForm
from .models import ComentarioContacto
from django.shortcuts import get_object_or_404
import datetime
#accedemos al modelo Alumnos que contiene la estructura de la tabla

# Create your views here.

def registros(request):
    alumnos=Alumnos.objects.all
    #all recupera todos los objetos del modelo(registro de la tabla alumnos)
    return render(request, "registros/principal.html",{'alumnos':alumnos})
#indicamos el lugar donde se renderizará el resultado de esta vista.
#y enviamos la lista de alumnos 

def regcontacto(request):
    comentarios = ComentarioContacto.objects.all()
    return render(request, 'registros/comentario.html', {'comentarios': comentarios})

def registrar(request):
    if request.method == 'POST':
        form = ComentarioContactoForm(request.POST)
        if form.is_valid():
            form.save()
            return render(request,'registros/contacto.html')
    form = ComentarioContacto()
    return render(request, 'registros/contacto.html',{'form': form})

def contacto(request):
    return render(request,"registros/contacto.html")

def eliminarComentarioContacto(request, id, confirmacion='registros/confirmarEliminacion.html'):
        comentario = get_object_or_404(ComentarioContacto, id=id)
        if request.method=='POST':
            comentario.delete()
            comentarios=ComentarioContacto.objects.all()
            return render(request,"registros/comentario.html",{'comentarios':comentarios})
        return render(request, confirmacion, {'object':comentario})


def consultarComentarioIndividual(request, id):
    comentario=ComentarioContacto.objects.get(id=id)
    return render(request,"registros/formEditarComentario.html",{'comentario':comentario})

def editarComentarioContacto(request, id):
    comentario = get_object_or_404(ComentarioContacto, id=id)
    form = ComentarioContactoForm(request.POST, instance=comentario)
    if form.is_valid():
        form.save()
        comentarios=ComentarioContacto.objects.all()
        return render(request,"registros/comentario.html",{'comentarios':comentarios})

    return render(request,"registros/formEditarComentario.html",{'comentario':comentario})

def consultar1(request):
    alumnos=Alumnos.objects.filter(carrera="TI")
    return render(request,"registros/consultas.html",{'alumnos':alumnos})

def consultar2(request):
    alumnos=Alumnos.objects.filter(carrera="TI").filter(turno="Matutino")
    return render(request,"registros/consultas.html",{'alumnos':alumnos})

def consultar3(request):
    alumnos=Alumnos.objects.all().only("matricula","nombre","carrera","turno","imagen")
    return render(request,"registros/consultas.html",{'alumnos':alumnos})

def consultar4(request):
    alumnos=Alumnos.objects.filter(turno__contains="Vesp")
    return render(request,"registros/consultas.html",{'alumnos':alumnos})

def consultar5(request):
    alumnos=Alumnos.objects.filter(nombre__in=["Juan","Ana"])
    return render(request,"registros/consultas.html",{'alumnos':alumnos})

def consultar6(request):
    fechaInicio=datetime.date(2022,7,1)
    fechaFin=datetime.date(2024,8,13)
    alumnos=Alumnos.objects.filter(created__range=(fechaInicio,fechaFin))
    return render(request,"registros/consultas.html",{'alumnos':alumnos})

def consultar7(request):
    alumnos=Alumnos.objects.filter(comentario__coment__contains="No inscrito")
    return render(request,"registros/consultas.html",{'alumnos':alumnos})

def consultasSQL(request):
    alumnos=Alumnos.objects.raw('SELECT id,matricula,nombre, carrera, turno, imagen FROM registros_alumnos WHERE carrera="TI" ORDER BY turno DESC')
    return render(request,"registros/consultas.html",{'alumnos':alumnos})