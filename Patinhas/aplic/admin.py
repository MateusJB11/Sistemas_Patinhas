from django.contrib import admin
from aplic.models import Gato, Cachorro, Tutor, Raca, Tipo, Evento, Voluntario, Veterinario, Clinica

@admin.register(Gato)
class GatoAdmin(admin.ModelAdmin):
    list_display = ('nome', 'peso')

@admin.register(Cachorro)
class CachorroAdmin(admin.ModelAdmin):
    list_display = ('nome', 'peso')



# Register your models here.
