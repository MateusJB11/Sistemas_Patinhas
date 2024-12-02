from django.contrib import admin
from .models import Raca, Gato, Cachorro, Veterinario, Tipo, Evento, Clinica, Usuario
from django.contrib.auth.admin import UserAdmin

field = list(UserAdmin.fieldsets)
field.append(
    ('Informações complementares', {'fields': ('cpf', 'telefone', 'data_nascimento')}),
    )
UserAdmin.fieldsets = tuple(field)
admin.site.register(Usuario, UserAdmin)

@admin.register(Raca)
class RacaAdmin(admin.ModelAdmin):
    list_display = ('nome_raca', 'descricao_raca')
@admin.register(Gato)
class GatoAdmin(admin.ModelAdmin):
    list_display = ('nome', 'raca', 'peso', 'sexo')
@admin.register(Cachorro)
class CachorroAdmin(admin.ModelAdmin):
    list_display = ('nome', 'peso', 'sexo')
@admin.register(Veterinario)
class VeterinarioAdmin(admin.ModelAdmin):
    list_display = ('crmv', 'telefone')
@admin.register(Tipo)
class TipoAdmin(admin.ModelAdmin):
    list_display = ('nome_tipo', 'descricao_tipo')
@admin.register(Evento)
class EventoAdmin(admin.ModelAdmin):
    list_display = ('descricao', 'data_inicio', 'data_fim', 'tipo')
@admin.register(Clinica)
class ClinicaAdmin(admin.ModelAdmin):
    list_display = ('nome_clinica', 'veterinario')



# Register your models here.
