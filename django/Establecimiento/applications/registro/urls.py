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

   
]
