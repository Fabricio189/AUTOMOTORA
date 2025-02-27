from django.contrib import admin
from .models import Marca, Automovil

# Register your models here.

class AutomovilAdmin(admin.ModelAdmin):
    list_display = ('Patente', 'Marca', 'Anio', 'Modelo')
    search_fields = ['Patente', 'Modelo']
    list_filter = ('Marca',)

admin.site.register(Marca)
admin.site.register(Automovil, AutomovilAdmin)
