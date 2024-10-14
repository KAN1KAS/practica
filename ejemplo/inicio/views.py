from django.shortcuts import render
from django.shortcuts import HttpResponse

# Create your views here.
def inicio(request):
    return render(request, 'inicio/inicio.html')

def nosotros(request):
    return render(request, 'inicio/nosotros.html')

def carrito(request):
    return render(request, 'inicio/carrito.html')