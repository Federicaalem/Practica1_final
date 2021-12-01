from django.contrib import admin
from .models import *

# Register your models here.
admin.site.register(EstablecimientoEducativo)

class PersonalAdmin(admin.ModelAdmin):
    list_display= (        
        'first_name',
        'last_name',                            
        'id',                      
    )
    
    search_fields = ('last_name', 'first_name')
    
admin.site.register(Personal, PersonalAdmin)


