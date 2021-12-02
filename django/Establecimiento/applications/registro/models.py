from django.db import models

# Create your models here.#clases

class EstablecimientoEducativo(models.Model):#hereda de la clase models.Model
    #definimos los atributos/campos
    #cmd tipo-> mchar
    name = models.CharField('Nombre', max_length=50)
    short_name = models.CharField('Nombre corto', max_length=50)
    
    #metaInformacion# informacion extra del modelo
    class Meta:
         verbose_name = 'Area'
         verbose_name_plural= 'Areas'
         ordering = ['name']
    
    #metodo
    def __str__(self):
        return self.name


class Personal(models.Model):
    """Model definition for Personal."""
    
    CARGO = (
        ('0', 'Docente'),
        ('1', 'No Docente'),
    )

    MATERIA = (
        ('0', 'Programacion 1'),
        ('1', 'Ingenieria de Software'),
        ('2', 'Practica 1'),
        ('3', 'Base de datos'),
    )

    OFICINA = (
        ('0', 'Preceptoria'),
        ('1', 'Direccion'),
        ('2', 'Coordinadocion'),
        ('3', 'Ayudante'),
    )

    first_name = models.CharField('Nombre', max_length=50)
    last_name= models.CharField('Apellido', max_length=50)
    years = models.IntegerField('Edad')
    #perfil = models.ImageField('Imagen de Perfil', upload_to=None, height_field=None, width_field=None, max_length=None)
    #perfil = models.ImageField(upload_to=None, height_field=None, width_field=None, max_length=100)
    job = models.CharField('Cargo', max_length=50, choices = CARGO)

    # = models.ForeignKey(EstablecimientoEducativo, on_delete=models.CASCADE)
  

    #si personal es Docente, agregar la materia a la cual pertenece.(habilitar opcion)       
    #si personal es NoDocente, agregar la oficina a la cual pertenece.(habilitar opcion)
    if job == '0':
        materia = models.CharField('Materia', unique=True, null=True, max_length=50, blank= True, choices = MATERIA)
    elif job == '1':
        oficina = models.CharField('Oficina',unique=True, null=True, max_length=50, blank= True, choices = OFICINA)
    
    
   
    class Meta:
        """Meta definition for Personal."""

        verbose_name = 'Personal'
        verbose_name_plural = 'Personales'

    def __str__(self):
        """Unicode representation of Personal."""
        return self.last_name + ', ' + self.first_name




