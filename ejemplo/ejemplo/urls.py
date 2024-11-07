"""
URL configuration for ejemplo project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from inicio import views
from ejercicios import views as views_ejercicios
from django.conf import settings

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views_ejercicios.principal, name='principal'),
    path('inicio/', views.inicio, name='inicio'),
    path('nosotros/', views.nosotros, name='nosotros'),
    path('carrito/', views.carrito, name='carrito'),
    path('mensajes/', views_ejercicios.mensajes, name='mensajes'),
    path('planetas/', views_ejercicios.planetas, name='planetas'),
    path('subir/', views_ejercicios.archivos, name='subir'),
]

if settings.DEBUG:
    from django.conf.urls.static import static 
    urlpatterns += static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT) 