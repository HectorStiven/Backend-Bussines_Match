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


from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin



# class UsuarioManager(BaseUserManager):
#     def create_user(self, correo_electronico, contrasena=None, **extra_fields):
#         if not correo_electronico:
#             raise ValueError('El usuario debe tener un correo electrónico')

#         correo_electronico = self.normalize_email(correo_electronico)
#         user = self.model(correo_electronico=correo_electronico, **extra_fields)
        
#         # Guardar la contraseña en tu campo `contrasena` sin usar el método `set_password`
#         if contrasena:
#             user.contrasena = contrasena

#         user.save(using=self._db)
#         return user

#     def create_superuser(self, correo_electronico, contrasena=None, **extra_fields):
#         extra_fields.setdefault('is_staff', True)
#         extra_fields.setdefault('is_superuser', True)
#         return self.create_user(correo_electronico, contrasena, **extra_fields)
    

class Usuario(AbstractBaseUser, PermissionsMixin):
    id = models.BigAutoField(primary_key=True)
    nombre = models.CharField(max_length=255)
    apellido = models.CharField(max_length=255)
    correo_electronico = models.EmailField(max_length=255, unique=True)
    contrasena = models.CharField(max_length=255)
    genero = models.CharField(max_length=50, null=True, blank=True)
    foto_perfil = models.URLField(max_length=255, null=True, blank=True)
    direccion = models.CharField(max_length=255)
    telefono = models.CharField(max_length=50, null=True, blank=True)
    pais = models.CharField(max_length=100, null=True, blank=True)
    ciudad = models.CharField(max_length=100, null=True, blank=True)
    fecha_nacimiento = models.DateField()
    numero_identificacion = models.CharField(max_length=50, unique=True)
    es_empresa = models.BooleanField(default=False)
    ultima_conexion = models.DateTimeField(null=True, blank=True)
    fecha_creacion = models.DateTimeField(auto_now_add=True)
    activo = models.BooleanField(default=True)
    notificaciones = models.BooleanField(default=True)

    # Avoid field clash by specifying related_name
    # groups = models.ManyToManyField(
    #     Group,
    #     related_name='usuario_set',
    #     blank=True,
    #     help_text='The groups this user belongs to.',
    #     verbose_name='groups',
    # )
    # user_permissions = models.ManyToManyField(
    #     Permission,
    #     related_name='usuario_set',
    #     blank=True,
    #     help_text='Specific permissions for this user.',
    #     verbose_name='user permissions',
    # )

    # objects = UsuarioManager()

    USERNAME_FIELD = 'correo_electronico'
    REQUIRED_FIELDS = ['nombre', 'apellido']

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





class Documento(models.Model):
    nombre = models.CharField(max_length=255)
    archivo = models.FileField(upload_to='dumes/')  # Almacenará los archivos en /media/dumes/
    # foto= models.ImageField(upload_to='fotos/')  # Almacenará las fotos en /media/fotos/
    subido_en = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name = 'Documento'
        verbose_name_plural = 'Documentos'
        db_table = 'T006Documento'