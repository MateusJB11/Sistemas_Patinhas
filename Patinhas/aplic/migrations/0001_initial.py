# Generated by Django 5.1.2 on 2024-10-09 03:12

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Animal',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=50)),
                ('peso', models.FloatField(blank=True, max_length='5', null=True, verbose_name='peso')),
                ('data_nascimento', models.DateField(blank=True, max_length=8, null=True)),
                ('sexo', models.CharField(choices=[('F', 'Femêa'), ('M', 'Macho')], max_length=1, verbose_name='sexo')),
                ('personalidade', models.CharField()),
            ],
        ),
        migrations.CreateModel(
            name='Pessoa',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=50)),
                ('cpf', models.CharField(blank=True, max_length=11, null=True, verbose_name='CPF')),
                ('data_nascimento', models.DateField(blank=True, max_length=8, null=True)),
                ('telefone', models.CharField(blank=True, max_length=11, null=True, verbose_name='Telefone')),
            ],
        ),
        migrations.CreateModel(
            name='Raca',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome_raca', models.CharField(blank=True, max_length=50, verbose_name='Raça')),
                ('descricao_raca', models.TextField(blank=True, max_length=50, verbose_name='Descrição')),
            ],
            options={
                'verbose_name_plural': 'Raças',
            },
        ),
        migrations.CreateModel(
            name='Tipo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome_tipo', models.CharField(max_length=50, verbose_name='Tipo')),
                ('descricao_tipo', models.TextField(verbose_name='Descrição')),
            ],
            options={
                'verbose_name_plural': 'Tipos',
            },
        ),
        migrations.CreateModel(
            name='Cachorro',
            fields=[
                ('animal_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='aplic.animal')),
                ('porte', models.CharField(max_length=50)),
            ],
            options={
                'verbose_name_plural': 'Cachorros',
            },
            bases=('aplic.animal',),
        ),
        migrations.CreateModel(
            name='Gato',
            fields=[
                ('animal_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='aplic.animal')),
            ],
            options={
                'verbose_name_plural': 'Gatos',
            },
            bases=('aplic.animal',),
        ),
        migrations.CreateModel(
            name='Tutor',
            fields=[
                ('pessoa_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='aplic.pessoa')),
                ('email', models.EmailField(blank=True, max_length=254, null=True, verbose_name='Email')),
                ('cep', models.CharField(blank=True, max_length=8, null=True, verbose_name='CEP')),
                ('logradouro', models.CharField(blank=True, max_length=50, null=True, verbose_name='Logradouro')),
                ('numero_casa', models.CharField(blank=True, max_length=15, null=True, verbose_name='Número')),
                ('complemento', models.CharField(blank=True, max_length=30, null=True, verbose_name='Complemento')),
                ('cidade', models.CharField(blank=True, max_length=20, null=True, verbose_name='Cidade')),
                ('estado', models.CharField(blank=True, max_length=2, null=True, verbose_name='UF')),
            ],
            options={
                'verbose_name_plural': 'Tutores',
            },
            bases=('aplic.pessoa',),
        ),
        migrations.CreateModel(
            name='Veterinario',
            fields=[
                ('pessoa_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='aplic.pessoa')),
                ('crmv', models.CharField(blank=True, max_length=10, null=True, verbose_name='CRMV')),
            ],
            bases=('aplic.pessoa',),
        ),
        migrations.CreateModel(
            name='Voluntario',
            fields=[
                ('pessoa_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='aplic.pessoa')),
            ],
            options={
                'verbose_name_plural': 'Voluntários',
            },
            bases=('aplic.pessoa',),
        ),
        migrations.AddField(
            model_name='animal',
            name='raca',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='aplic.raca'),
        ),
        migrations.CreateModel(
            name='Evento',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('data_inicio', models.DateField(blank=True, max_length=8, null=True, verbose_name='Data Início')),
                ('data_fim', models.DateField(blank=True, max_length=8, null=True, verbose_name='Data Fim')),
                ('descricao', models.CharField(max_length=50, verbose_name='Descrição do Evento')),
                ('tipo', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='aplic.tipo')),
            ],
            options={
                'verbose_name_plural': 'Eventos',
            },
        ),
        migrations.CreateModel(
            name='Clinica',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome_clinica', models.CharField(blank=True, max_length=15, null=True, verbose_name='Clínica')),
                ('data_entrada', models.DateField(blank=True, max_length=8, null=True)),
                ('data_saida', models.DateField(blank=True, max_length=8, null=True)),
                ('veterinario', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='aplic.veterinario')),
            ],
            options={
                'verbose_name_plural': 'Clínicas',
            },
        ),
    ]
