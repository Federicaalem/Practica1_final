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
from .models import PersonalDocente, PersonalNoDocente
#importa models significa que estamos importando desde un archivo que esta 
#en el mismo directorio "models.py" 


# Create your views here.
#estas vistas se definen a traves de clases


#READ
#PERSONAL DOCENTE
class PersonalDocenteListViewAll(ListView):
    model = PersonalDocente
    template_name = "registroDocente/list_All.html"
    ordering = 'last_name'
    context_object_name = 'lista'
    paginate_by = 4

    def get_queryset(self):
        palabra_clave = self.request.GET.get('kword', '')
        lista = PersonalDocente.objects.filter(
            last_name__icontains = palabra_clave
        )
        return lista

class PersonalDocenteDetailView(DetailView):
    model = PersonalDocente
    template_name = "registroDocente/detalle.html"
    context_object_name = 'detalle_Docente'

#vista de Exito
class SuccessView(TemplateView):
    template_name = "registroDocente/exito.html"


class PersonalDocenteCreateView(CreateView):
    model = PersonalDocente
    template_name = "registroDocente/alta.html"
    #definir campos

    fields = (
        'last_name',
        'first_name',
        'materia',  
        'perfil',      
        'years',
        
    )

    success_url= reverse_lazy('registro_app:listar-personal-docente')
    #para guardar en la base de datos
    def form_valid(self, form):
        personalDocente= form.save(commit = False)
        personalDocente.full_name = personalDocente.first_name + ' ' + personalDocente.last_name
        personalDocente.save()
        return super(PersonalDocenteCreateView, self).form_valid(form)


class PersonalDocenteUpdateView(UpdateView):
    model = PersonalDocente
    template_name = "registroDocente/update.html"

    fields = (
        'last_name',
        'first_name',
        'materia',
        'years',  
        'perfil',      
    )

    success_url= reverse_lazy('registro_app:listar-personal-docente')
    #para guardar en la base de datos
    def form_valid(self, form):
        personalDocente= form.save(commit = False)
        personalDocente.full_name = personalDocente.first_name + ' ' + personalDocente.last_name
        personalDocente.save()
        return super(PersonalDocenteUpdateView, self).form_valid(form)

class PersonalDocenteDeleteView(DeleteView):
    model = PersonalDocente
    template_name = "registroDocente/delete.html"
    success_url= reverse_lazy('registro_app:listar-personal-docente')










class PersonalNoDocenteListViewAll(ListView):
    model = PersonalNoDocente
    template_name = "registroNoDocente/list_All.html"
    ordering = 'last_name'
    context_object_name = 'lista'
    paginate_by = 4

    def get_queryset(self):
        palabra_clave = self.request.GET.get('kword', '')
        lista = PersonalNoDocente.objects.filter(
            last_name__icontains = palabra_clave
            
        )
        return lista


class PersonalNoDocenteDetailView(DetailView):
    model = PersonalNoDocente
    template_name = "registroNoDocente/detalle.html"
    context_object_name = 'detalle_NoDocente'


#vista de Exito
class SuccessView(TemplateView):
    template_name = "registroNoDocente/exito.html"


class PersonalNoDocenteCreateView(CreateView):
    model = PersonalNoDocente
    template_name = "registroNoDocente/alta.html"
    #definir campos

    fields = (
        'last_name',
        'first_name',
        'oficina',        
        'years',
        'perfil',
        
    )

    success_url= reverse_lazy('registro_app:listar-personal-no-docente')
    #para guardar en la base de datos
    def form_valid(self, form):
        personalNoDocente= form.save(commit = False)
        personalNoDocente.full_name = personalNoDocente.first_name + ' ' + personalNoDocente.last_name
        personalNoDocente.save()
        return super(PersonalNoDocenteCreateView, self).form_valid(form)


class PersonalNoDocenteUpdateView(UpdateView):
    model = PersonalNoDocente
    template_name = "registroNoDocente/update.html"

    fields = (
        'last_name',
        'first_name',
        'oficina',
        'years',    
        'perfil',     
    )

    success_url= reverse_lazy('registro_app:listar-personal-no-docente')
    #para guardar en la base de datos
    def form_valid(self, form):
        personalNoDocente= form.save(commit = False)
        personalNoDocente.full_name = personalNoDocente.first_name + ' ' + personalNoDocente.last_name
        personalNoDocente.save()
        return super(PersonalNoDocenteUpdateView, self).form_valid(form)

class PersonalNoDocenteDeleteView(DeleteView):
    model = PersonalNoDocente
    template_name = "registroNoDocente/delete.html"
    success_url= reverse_lazy('registro_app:listar-personal-no-docente')



class VistaPrincipalView(TemplateView):
    template_name = "index.html"
