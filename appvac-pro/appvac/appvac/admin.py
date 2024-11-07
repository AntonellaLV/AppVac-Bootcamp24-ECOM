from django.contrib import admin
from .models import Proyecto

# Register your models here.

@admin.register(Proyecto)
class ProyectoAdmin(admin.ModelAdmin):
    list_display = ('titulo', 'fecha', 'enlace')  # Campos a mostrar en la lista
    search_fields = ('titulo',)  # Habilitar búsqueda por título
