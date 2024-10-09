from django.db import models

class Usuario(models.Model):
    id = models.BigAutoField(primary_key=True)  # Identificador único del usuario
    nombre = models.CharField(max_length=255)  # Nombre del usuario
    apellido = models.CharField(max_length=255)  # Apellido del usuario
    correo_electronico = models.EmailField(max_length=255, unique=True)  # Correo electrónico del usuario
    contrasena = models.CharField(max_length=255)  # Contraseña del usuario
    genero = models.CharField(max_length=50)  # Género del usuario
    estado = models.CharField(max_length=50)  # Estado del usuario
    foto_perfil = models.URLField(max_length=255, blank=True, null=True)  # URL de la foto de perfil del usuario
    direccion = models.CharField(max_length=255)  # Dirección del usuario
    fecha_nacimiento = models.DateField()  # Fecha de nacimiento del usuario
    numero_identificacion = models.CharField(max_length=50, unique=True)  # Número de identificación del usuario
    es_empresa = models.BooleanField(default=False)  # Indica si el usuario es una empresa

    class Meta:
        verbose_name = 'Usuario'
        verbose_name_plural = 'Usuarios'
        db_table = 'T001Usuario'  # Nombre de la tabla en la base de datos

class Categoria(models.Model):
    id = models.BigAutoField(primary_key=True)  # Identificador único de la categoría
    nombre = models.CharField(max_length=255, unique=True)  # Nombre de la categoría
    descripcion = models.TextField(max_length=500)  # Descripción de la categoría
    subcategoria = models.ForeignKey('Subcategoria', on_delete=models.CASCADE, null=True, blank=True)  # Subcategoría asociada

    class Meta:
        verbose_name = 'Categoría'
        verbose_name_plural = 'Categorías'
        db_table = 'T002Categoria'  # Nombre de la tabla en la base de datos

class Subcategoria(models.Model):
    id = models.BigAutoField(primary_key=True)  # Identificador único de la subcategoría
    nombre = models.CharField(max_length=255, unique=True)  # Nombre de la subcategoría
    descripcion = models.TextField(max_length=500)  # Descripción de la subcategoría

    class Meta:
        verbose_name = 'Subcategoría'
        verbose_name_plural = 'Subcategorías'
        db_table = 'T003Subcategoria'  # Nombre de la tabla en la base de datos

class TipoEmpresa(models.Model):
    id = models.BigAutoField(primary_key=True)  # Identificador único del tipo de empresa
    nombre = models.CharField(max_length=255, unique=True)  # Nombre del tipo de empresa
    descripcion = models.TextField(max_length=500)  # Descripción del tipo de empresa

    class Meta:
        verbose_name = 'Tipo Empresa'
        verbose_name_plural = 'Tipos Empresa'
        db_table = 'T006TipoEmpresa'  # Nombre de la tabla en la base de datos

class Empresa(models.Model):
    id = models.BigAutoField(primary_key=True)  # Identificador único de la empresa
    foto_perfil = models.URLField(max_length=255, blank=True, null=True)  # URL de la foto de perfil de la empresa
    nombre = models.CharField(max_length=255)  # Nombre de la empresa
    direccion = models.CharField(max_length=255)  # Dirección de la empresa
    telefono = models.CharField(max_length=50)  # Teléfono de contacto de la empresa
    correo_electronico = models.EmailField(max_length=255, unique=True)  # Correo electrónico de la empresa
    fecha_registro = models.DateField()  # Fecha de registro de la empresa
    numero_identificacion = models.CharField(max_length=50, unique=True)  # Número de identificación de la empresa
    tipo_empresa = models.ForeignKey(TipoEmpresa, on_delete=models.CASCADE)  # Tipo de empresa
    paginawed = models.URLField(max_length=255, blank=True, null=True)  # URL de la página web de la empresa
    contacto = models.CharField(max_length=255)  # Nombre del contacto principal de la empresa

    class Meta:
        verbose_name = 'Empresa'
        verbose_name_plural = 'Empresas'
        db_table = 'T007Empresa'  # Nombre de la tabla en la base de datos

class Match(models.Model):
    id = models.BigAutoField(primary_key=True)  # Identificador único del match
    usuario = models.ForeignKey(Usuario, related_name='matches', on_delete=models.CASCADE)  # Usuario asociado al match
    empresa = models.ForeignKey(Empresa, on_delete=models.CASCADE)  # Empresa asociada al match
    fecha_match = models.DateTimeField()  # Fecha del match
    categoria = models.ForeignKey(Categoria, on_delete=models.CASCADE)  # Categoría asociada al match
    etapa = models.CharField(max_length=50)  # Etapa del match
    asunto = models.CharField(max_length=255)  # Asunto del match
    descripcion = models.TextField(max_length=500)  # Descripción del match
    postulados = models.JSONField(blank=True, null=True)  # Datos adicionales en formato JSON

    class Meta:
        verbose_name = 'Match'
        verbose_name_plural = 'Matches'
        db_table = 'T004Match'  # Nombre de la tabla en la base de datos

class Interes(models.Model):
    id = models.BigAutoField(primary_key=True)  # Identificador único del interés
    nombre = models.CharField(max_length=255, unique=True)  # Nombre del interés
    descripcion = models.TextField(max_length=500)  # Descripción del interés
    usuario = models.ForeignKey(Usuario, on_delete=models.CASCADE)  # Usuario asociado al interés

    class Meta:
        verbose_name = 'Interés'
        verbose_name_plural = 'Intereses'
        db_table = 'T005Interes'  # Nombre de la tabla en la base de datos
