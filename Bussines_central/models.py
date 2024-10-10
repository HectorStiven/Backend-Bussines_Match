from django.db import models

# Modelo Empresa
class Empresa(models.Model):
    id = models.BigAutoField(primary_key=True)  # Identificador único de la empresa
    nombre_legal = models.CharField(max_length=255, unique=True)  # Nombre legal de la empresa
    numero_registro = models.CharField(max_length=50, unique=True)  # Número de registro de la empresa
    tipo_empresa = models.CharField(max_length=100)  # Tipo de empresa (e.g., SRL, SA, etc.)
    direccion_fiscal = models.CharField(max_length=255)  # Dirección fiscal de la empresa
    telefono_contacto = models.CharField(max_length=50)  # Teléfono de contacto de la empresa
    correo_contacto = models.EmailField(max_length=255, unique=True)  # Correo electrónico de contacto
    pagina_web = models.URLField(max_length=255, null=True, blank=True)  # Página web de la empresa
    fecha_creacion = models.DateTimeField(auto_now_add=True)  # Fecha de creación del registro

    class Meta:
        verbose_name = 'Empresa'
        verbose_name_plural = 'Empresas'
        db_table = 'T007Empresa'  # Nombre de la tabla en la base de datos


# Modelo Usuario
class Usuario(models.Model):
    id = models.BigAutoField(primary_key=True)  # Identificador único del usuario
    nombre = models.CharField(max_length=255)  # Nombre del usuario
    apellido = models.CharField(max_length=255)  # Apellido del usuario
    correo_electronico = models.EmailField(max_length=255, unique=True)  # Correo electrónico
    contrasena = models.CharField(max_length=255)  # Contraseña del usuario
    genero = models.CharField(max_length=50, null=True, blank=True)  # Género (opcional)
    foto_perfil = models.URLField(max_length=255, null=True, blank=True)  # Foto de perfil
    direccion = models.CharField(max_length=255)  # Dirección del usuario
    telefono = models.CharField(max_length=50, null=True, blank=True)  # Teléfono (opcional)
    pais = models.CharField(max_length=100, null=True, blank=True)  # País (opcional)
    ciudad = models.CharField(max_length=100, null=True, blank=True)  # Ciudad (opcional)
    fecha_nacimiento = models.DateField()  # Fecha de nacimiento
    numero_identificacion = models.CharField(max_length=50, unique=True)  # Número de identificación
    es_empresa = models.BooleanField(default=False)  # Indica si es una empresa
    empresa = models.ForeignKey(Empresa, null=True, blank=True, on_delete=models.SET_NULL)  # Relación con Empresa
    ultima_conexion = models.DateTimeField(null=True, blank=True)  # Última conexión
    fecha_creacion = models.DateTimeField(auto_now_add=True)  # Fecha de creación
    activo = models.BooleanField(default=True)  # Estado activo/inactivo
    notificaciones = models.BooleanField(default=True)  # Recibir notificaciones

    class Meta:
        verbose_name = 'Usuario'
        verbose_name_plural = 'Usuarios'
        db_table = 'T001Usuario'

# Modelo Subcategoria
class Subcategoria(models.Model):
    id = models.BigAutoField(primary_key=True)  # Identificador único de la subcategoría
    nombre = models.CharField(max_length=255, unique=True)  # Nombre de la subcategoría
    descripcion = models.TextField(max_length=500)  # Descripción de la subcategoría

    class Meta:
        verbose_name = 'Subcategoría'
        verbose_name_plural = 'Subcategorías'
        db_table = 'T003Subcategoria'


# Modelo Categoria
class Categoria(models.Model):
    id = models.BigAutoField(primary_key=True)  # Identificador único de la categoría
    nombre = models.CharField(max_length=255, unique=True)  # Nombre de la categoría
    descripcion = models.TextField(max_length=500)  # Descripción de la categoría
    subcategoria = models.ForeignKey(Subcategoria, null=True, blank=True, on_delete=models.SET_NULL)  # Subcategoría asociada

    class Meta:
        verbose_name = 'Categoría'
        verbose_name_plural = 'Categorías'
        db_table = 'T002Categoria'


class Match(models.Model):
    id = models.BigAutoField(primary_key=True)  # Identificador único del match
    usuario = models.ForeignKey(Usuario, related_name='matches', on_delete=models.CASCADE)  # Usuario asociado al match
    usuario_2 = models.ForeignKey(Usuario, related_name='matches_with', on_delete=models.CASCADE)  # Segundo usuario asociado
    fecha_match = models.DateTimeField(auto_now_add=True)  # Fecha del match
    categoria = models.ForeignKey(Categoria, on_delete=models.CASCADE)  # Categoría asociada
    etapa = models.CharField(max_length=50)  # Etapa del match
    asunto = models.CharField(max_length=255)  # Asunto del match
    descripcion = models.TextField(max_length=500)  # Descripción del match

    class Meta:
        verbose_name = 'Match'
        verbose_name_plural = 'Matches'
        db_table = 'T004Match'

# Modelo Interes
class Interes(models.Model):
    id = models.BigAutoField(primary_key=True)  # Identificador único del interés
    nombre = models.CharField(max_length=255, unique=True)  # Nombre del interés
    descripcion = models.TextField(max_length=500)  # Descripción del interés
    usuario = models.ForeignKey(Usuario, on_delete=models.CASCADE)  # Usuario asociado

    class Meta:
        verbose_name = 'Interés'
        verbose_name_plural = 'Intereses'
        db_table = 'T005Interes'
