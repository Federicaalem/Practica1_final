from django.contrib import admin
from django.urls import path, include
from . import views#el punto hace que importe todo el contenido del archivo views

#nombre a la app
app_name= 'registro_app'
urlpatterns = [
    
    #DOCENTES
    path(
        'listar-personal-docente/',
        views.PersonalDocenteListViewAll.as_view(),        
        name='listar-personal-docente'
    ),

   path(
        'detalle-docente/<pk>/',
        views.PersonalDocenteDetailView.as_view(),
        name='detalle_Docente'
    ),

    path(
        'exito-docente/',
        views.SuccessView.as_view(),
        name='exito'
    ),

    path(
        'alta-docente/',
        views.PersonalDocenteCreateView.as_view(),
        name='alta_Docente'
    ),

     path(
        'update-docente/<pk>/',
        views.PersonalDocenteUpdateView.as_view(),
        name='update_Docente'
    ),

    path(
        'delete-docente/<pk>/',
        views.PersonalDocenteDeleteView.as_view(),
        name='delete_Docente'
    ),





    #No Docente
    path(
        'listar-personal-no-docente/',
        views.PersonalNoDocenteListViewAll.as_view(),        
        name='listar-personal-no-docente'
    ),

   path(
        'detalle-no-docente/<pk>/',
        views.PersonalNoDocenteDetailView.as_view(),
        name='detalle_NoDocente'
    ),

    path(
        'exito-no-docente/',
        views.SuccessView.as_view(),
        name='exito'
    ),

    path(
        'alta-no-docente/',
        views.PersonalNoDocenteCreateView.as_view(),
        name='alta_NoDocente'
    ),

     path(
        'update-no-docente/<pk>/',
        views.PersonalNoDocenteUpdateView.as_view(),
        name='update_NoDocente'
    ),

    path(
        'delete-no-docente/<pk>/',
        views.PersonalNoDocenteDeleteView.as_view(),
        name='delete_NoDocente'
    ),


    path(
        '',
        views.VistaPrincipalView.as_view(),
        name="index"
    ),
]

