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


#READ
class PersonalListViewAll(ListView):
    model = Personal
    template_name = "registro/list_All.html"
    ordering = 'last_name'
    context_object_name = 'lista'

class PersonalDetailView(DetailView):
    model = Personal
    template_name = "registro/detalle.html"
    context_object_name = 'detalle'



#vista de Exito

class SuccessView(TemplateView):
    template_name = "registro/exito.html"


class PersonalCreateView(CreateView):
    model = Personal
    template_name = "registro/alta.html"
    #definir campos

    fields = (
        'last_name',
        'first_name',
        'job',
        'years',
        
    )

    success_url= reverse_lazy('registro_app:exito')
    #para guardar en la base de datos
    def form_valid(self, form):
        personal= form.save(commit = False)
        personal.full_name = personal.first_name + ' ' + personal.last_name
        personal.save()
        return super(PersonalCreateView, self).form_valid(form)


class PersonalUpdateView(UpdateView):
    model = Personal
    template_name = "registro/update.html"

    fields = (
        'last_name',
        'first_name',
        'job',
        'years',        
    )

    success_url= reverse_lazy('registro_app:exito')
    #para guardar en la base de datos
    def form_valid(self, form):
        personal= form.save(commit = False)
        personal.full_name = personal.first_name + ' ' + personal.last_name
        personal.save()
        return super(PersonalUpdateView, self).form_valid(form)

class PersonalDeleteView(DeleteView):
    model = Personal
    template_name = "registro/delete.html"
    success_url= reverse_lazy('registro_app:exito')


