from django.contrib import admin
from django.urls import path, include
from . import views#el punto hace que importe todo el contenido del archivo views

#nombre a la app
app_name= 'registro_app'
urlpatterns = [
    path(
        'listar-personal/',
        views.PersonalListViewAll.as_view(),
        name='listar-personal'
    ),

   path(
        'detalle/<pk>/',
        views.PersonalDetailView.as_view(),
        name='detalle'
    ),

    path(
        'exito/',
        views.SuccessView.as_view(),
        name='exito'
    ),

    path(
        'alta/',
        views.PersonalCreateView.as_view(),
        name='alta'
    ),

     path(
        'update/<pk>/',
        views.PersonalUpdateView.as_view(),
        name='update'
    ),

    path(
        'delete/<pk>/',
        views.PersonalDeleteView.as_view(),
        name='delete'
    ),


]

