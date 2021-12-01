from django.shortcuts import render
from django.views.generic import (
    CreateView,
    ListView,
    DetailView,
    TemplateView,
    UpdateView,
    DeleteView,
)
#libreria, nos servira para direccionar una
#pagina hacia otra validando lo que hemos hecho(exitosamente).

from django.urls import reverse_lazy
from .models import Personal
#importa models significa que estamos importando desde un archivo que esta 
#en el mismo directorio "models.py" 


# Create your views here.
#estas vistas se definen a traves de clases


class PersonalListViewAll(ListView):
    model = Personal
    template_name = "registro/list_All.html"
    ordering = 'last_name'
    context_object_name = 'lista'




