from django.db import models

# Create your models here.#clases

class EstablecimientoEducativo(models.Model):#hereda de la clase models.Model
    #definimos los atributos/campos
    #cmd tipo-> mchar
    name = models.CharField('Nombre', max_length=50)
    short_name = models.CharField('Nombre corto', max_length=50)
    
    #metaInformacion# informacion extra del modelo
    class Meta:
         verbose_name = 'Materia'
         verbose_name_plural= 'Materias'
         ordering = ['name']
    
    #metodo
    def __str__(self):
        return self.name

class EstablecimientoEducativo2(models.Model):#hereda de la clase models.Model
    #definimos los atributos/campos
    #cmd tipo-> mchar
    name = models.CharField('Nombre', max_length=50)
    short_name = models.CharField('Nombre corto', max_length=50)
    
    #metaInformacion# informacion extra del modelo
    class Meta:
         verbose_name = 'Oficina'
         verbose_name_plural= 'Oficinas'
         ordering = ['name']
    
    #metodo
    def __str__(self):
        return self.name

 

class PersonalDocente(models.Model):
    """Model definition for PersonalDocente."""
    
    
    first_name = models.CharField('Nombre', max_length=50)
    last_name= models.CharField('Apellido', max_length=50)
    years = models.IntegerField('Edad')
    
    materia = models.ForeignKey(EstablecimientoEducativo, null=True,  on_delete=models.CASCADE)
    perfil = models.ImageField('Imagen de Perfil', upload_to='registro', height_field=None, width_field=None, max_length=None )

    
    class Meta:
        """Meta definition for PersonalDocente."""

        verbose_name = 'PersonalDocentes'
        verbose_name_plural = 'PersonalDocente'

    def __str__(self):
        """Unicode representation of PersonalDocente."""
        return self.last_name + ', ' + self.first_name



class PersonalNoDocente(models.Model):
    """Model definition for PersonalNoDocente."""
    

    first_name = models.CharField('Nombre', max_length=50)
    last_name= models.CharField('Apellido', max_length=50)
    years = models.IntegerField('Edad')
    
    oficina = models.ForeignKey(EstablecimientoEducativo2, null=True, on_delete=models.CASCADE)
    perfil = models.ImageField('Imagen de Perfil', upload_to='registro', height_field=None, width_field=None, max_length=None)
    
    
    class Meta:
        """Meta definition for PersonalDocente."""

        verbose_name = 'PersonalNoDocentes'
        verbose_name_plural = 'PersonalNoDocente'

    def __str__(self):
        """Unicode representation of PersonalDocente."""
        return self.last_name + ', ' + self.first_name


