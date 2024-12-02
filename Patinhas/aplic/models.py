import uuid
from django.db import models
from stdimage.models import StdImageField
from django.contrib.auth.models import AbstractUser



def get_file_path(_instance, filename):
    ext = filename.split('.')[-1]
    filename = f'{uuid.uuid4()}.{ext}'
    return filename

class SexOptions(models.TextChoices):
    FEMALE = 'F', 'Femêa'
    MALE = 'M', 'Macho'


class Raca(models.Model):
    nome_raca = models.CharField(("Raça"), max_length=50, blank=True, null=False)
    descricao_raca = models.TextField(('Descrição'), max_length=50, blank=True, null=False)

    class Meta:
        verbose_name_plural = 'Raças'

    def __str__(self):
        return self.nome_raca


class Animal(models.Model):
    nome = models.CharField(max_length=50)
    peso = models.FloatField(('peso'), blank=True, null=True, max_length="5")
    data_nascimento = models.DateField(max_length=8, blank=True, null=True)
    sexo = models.CharField(('sexo'), max_length=1, choices=SexOptions.choices)
    descricao = models.CharField(('descrição'), max_length=300, blank=True, null=True)
    raca = models.ForeignKey(Raca, on_delete=models.CASCADE, null=True)
    imagem = StdImageField(('Imagem'), null=True, blank=True, upload_to=get_file_path, variations={'thumb': {'width': 420, 'height': 260, 'crop': True}})


class Cachorro(Animal):
    porte = models.CharField(max_length=50)

    class Meta:
        verbose_name_plural = 'Cachorros'

    def __str__(self):
        return self.nome


class Gato(Animal):
    class Meta:
        verbose_name_plural = 'Gatos'

    def __str__(self):
        return self.nome


class Usuario(AbstractUser):
    cpf = models.CharField(('CPF'), max_length=11, blank=True, null=True)
    data_nascimento = models.DateField(max_length=8, blank=True, null=True)
    telefone = models.CharField(('Telefone'), max_length=11, blank=True, null=True)



class Veterinario(models.Model):
    crmv = models.CharField(("CRMV"), max_length=10, blank=True, null=True)
    telefone = models.CharField(('Telefone'), max_length=11, blank=True, null=True)

class Tipo(models.Model):
    nome_tipo = models.CharField(("Tipo"), max_length=50)
    descricao_tipo = models.TextField('Descrição')

    class Meta:
        verbose_name_plural = 'Tipos'

    def __str__(self):
        return self.nome_tipo

class Evento(models.Model):
    data_inicio = models.DateField(('Data Início'), max_length=8, blank=True, null=True)
    data_fim = models.DateField(('Data Fim'),max_length=8, blank=True, null=True)
    descricao = models.CharField(('Descrição do Evento'), max_length=50)
    tipo = models.ForeignKey(Tipo, on_delete=models.CASCADE)

    class Meta:
        verbose_name_plural = 'Eventos'

    def __str__(self):
        return self.tipo


class Clinica(models.Model):
    nome_clinica = models.CharField(("Clínica"), max_length=15, blank=True, null=True)
    veterinario = models.ForeignKey(Veterinario, on_delete=models.CASCADE, null=True)
    logradouro = models.CharField(('Logradouro'), max_length=50, blank=True, null=True)
    numero_logradouro = models.IntegerField(('Número'), blank=True, null=True)
    complemento = models.CharField(('Complemento'), max_length=30, blank=True, null=True)
    bairro = models.CharField(('Bairro'), max_length=50, blank=True, null=True)
    cidade = models.CharField(('Cidade'), max_length=20, blank=True, null=True)
    estado = models.CharField(('Estado'), max_length=2, blank=True, null=True)
    cep = models.IntegerField(('CEP'), blank=True, null=True)

    class Meta:
        verbose_name_plural = 'Clínicas'

    def __str__(self):
        return self.veterinario



# Create your models here.
