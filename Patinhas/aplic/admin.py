from django.contrib import admin
from .models import Raca, Gato, Cachorro, Tutor, Voluntario, Veterinario, Tipo, Evento, Clinica, Endereco

@admin.register(Raca)
class RacaAdmin(admin.ModelAdmin):
    list_display = ('nome_raca', 'descricao_raca')
@admin.register(Gato)
class GatoAdmin(admin.ModelAdmin):
    list_display = ('nome', 'raca', 'peso', 'sexo')
@admin.register(Cachorro)
class CachorroAdmin(admin.ModelAdmin):
    list_display = ('nome', 'peso', 'sexo')
@admin.register(Tutor)
class TutorAdmin(admin.ModelAdmin):
    list_display = ('nome', 'cpf', 'telefone', 'email')
@admin.register(Voluntario)
class VoluntarioAdmin(admin.ModelAdmin):
    list_display = ('nome','telefone')
@admin.register(Veterinario)
class VeterinarioAdmin(admin.ModelAdmin):
    list_display = ('nome', 'crmv', 'telefone')
@admin.register(Tipo)
class TipoAdmin(admin.ModelAdmin):
    list_display = ('nome_tipo', 'descricao_tipo')
@admin.register(Evento)
class EventoAdmin(admin.ModelAdmin):
    list_display = ('descricao', 'data_inicio', 'data_fim', 'tipo')
@admin.register(Clinica)
class ClinicaAdmin(admin.ModelAdmin):
    list_display = ('nome_clinica', 'veterinario')
@admin.register(Endereco)
class EnderecoAdmin(admin.ModelAdmin):
    list_display = ('logradouro', 'numero_logradouro', 'complemento')



# Register your models here.
