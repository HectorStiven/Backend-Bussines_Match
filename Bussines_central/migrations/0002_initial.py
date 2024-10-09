# Generated by Django 5.1.1 on 2024-10-09 01:10

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('Bussines_central', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Subcategoria',
            fields=[
                ('id', models.BigAutoField(primary_key=True, serialize=False)),
                ('nombre', models.CharField(max_length=255, unique=True)),
                ('descripcion', models.TextField(max_length=500)),
            ],
            options={
                'verbose_name': 'Subcategoría',
                'verbose_name_plural': 'Subcategorías',
                'db_table': 'T003Subcategoria',
            },
        ),
        migrations.CreateModel(
            name='TipoEmpresa',
            fields=[
                ('id', models.BigAutoField(primary_key=True, serialize=False)),
                ('nombre', models.CharField(max_length=255, unique=True)),
                ('descripcion', models.TextField(max_length=500)),
            ],
            options={
                'verbose_name': 'Tipo Empresa',
                'verbose_name_plural': 'Tipos Empresa',
                'db_table': 'T006TipoEmpresa',
            },
        ),
        migrations.CreateModel(
            name='Usuario',
            fields=[
                ('id', models.BigAutoField(primary_key=True, serialize=False)),
                ('nombre', models.CharField(max_length=255)),
                ('apellido', models.CharField(max_length=255)),
                ('correo_electronico', models.EmailField(max_length=255, unique=True)),
                ('contrasena', models.CharField(max_length=255)),
                ('genero', models.CharField(max_length=50)),
                ('estado', models.CharField(max_length=50)),
                ('foto_perfil', models.URLField(blank=True, max_length=255, null=True)),
                ('direccion', models.CharField(max_length=255)),
                ('fecha_nacimiento', models.DateField()),
                ('numero_identificacion', models.CharField(max_length=50, unique=True)),
                ('es_empresa', models.BooleanField(default=False)),
            ],
            options={
                'verbose_name': 'Usuario',
                'verbose_name_plural': 'Usuarios',
                'db_table': 'T001Usuario',
            },
        ),
        migrations.CreateModel(
            name='Categoria',
            fields=[
                ('id', models.BigAutoField(primary_key=True, serialize=False)),
                ('nombre', models.CharField(max_length=255, unique=True)),
                ('descripcion', models.TextField(max_length=500)),
                ('subcategoria', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='Bussines_central.subcategoria')),
            ],
            options={
                'verbose_name': 'Categoría',
                'verbose_name_plural': 'Categorías',
                'db_table': 'T002Categoria',
            },
        ),
        migrations.CreateModel(
            name='Empresa',
            fields=[
                ('id', models.BigAutoField(primary_key=True, serialize=False)),
                ('foto_perfil', models.URLField(blank=True, max_length=255, null=True)),
                ('nombre', models.CharField(max_length=255)),
                ('direccion', models.CharField(max_length=255)),
                ('telefono', models.CharField(max_length=50)),
                ('correo_electronico', models.EmailField(max_length=255, unique=True)),
                ('fecha_registro', models.DateField()),
                ('numero_identificacion', models.CharField(max_length=50, unique=True)),
                ('paginawed', models.URLField(blank=True, max_length=255, null=True)),
                ('contacto', models.CharField(max_length=255)),
                ('tipo_empresa', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Bussines_central.tipoempresa')),
            ],
            options={
                'verbose_name': 'Empresa',
                'verbose_name_plural': 'Empresas',
                'db_table': 'T007Empresa',
            },
        ),
        migrations.CreateModel(
            name='Match',
            fields=[
                ('id', models.BigAutoField(primary_key=True, serialize=False)),
                ('fecha_match', models.DateTimeField()),
                ('etapa', models.CharField(max_length=50)),
                ('asunto', models.CharField(max_length=255)),
                ('descripcion', models.TextField(max_length=500)),
                ('postulados', models.JSONField(blank=True, null=True)),
                ('categoria', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Bussines_central.categoria')),
                ('empresa', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Bussines_central.empresa')),
                ('usuario', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='matches', to='Bussines_central.usuario')),
            ],
            options={
                'verbose_name': 'Match',
                'verbose_name_plural': 'Matches',
                'db_table': 'T004Match',
            },
        ),
        migrations.CreateModel(
            name='Interes',
            fields=[
                ('id', models.BigAutoField(primary_key=True, serialize=False)),
                ('nombre', models.CharField(max_length=255, unique=True)),
                ('descripcion', models.TextField(max_length=500)),
                ('usuario', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Bussines_central.usuario')),
            ],
            options={
                'verbose_name': 'Interés',
                'verbose_name_plural': 'Intereses',
                'db_table': 'T005Interes',
            },
        ),
    ]
