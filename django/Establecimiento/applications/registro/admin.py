from django.contrib import admin
from .models import *

# Register your models here.
admin.site.register(EstablecimientoEducativo)

class PersonalDocenteAdmin(admin.ModelAdmin):
    list_display= (        
        'first_name',
        'last_name',
        'materia',        
        'id',                              
    )
    

admin.site.register(PersonalDocente, PersonalDocenteAdmin)



class PersonalNoDocenteAdmin(admin.ModelAdmin):
    list_display= (        
        'first_name',
        'last_name',
        'oficina',        
        'id',                              
    )
    

admin.site.register(PersonalNoDocente, PersonalNoDocenteAdmin)


#search_fields = ('last_name', 'first_name')




