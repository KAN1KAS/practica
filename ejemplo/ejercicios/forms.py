from .models import Archivos,Planetas
from django.forms import ModelForm, ClearableFileInput

class CustomClearableFileInput(ClearableFileInput):
    template_with_clear='<br> <label for="%(clear_checkbox_id)s">%(clear_checkbox_id)s</label> %(clear)s'

class FormArchivos(ModelForm):
    class Meta:
        model=Archivos
        fields=('titulo','descripcion', 'archivo')
        widgets={
            'archivo': CustomClearableFileInput
        } 

class FormPlanetas(ModelForm):
    class Meta:
        model=Planetas
        fields=['archivo']
        widgets={
            'archivo': CustomClearableFileInput
        } 