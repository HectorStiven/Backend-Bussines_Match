from rest_framework import serializers
from .models import Documento, Usuario, Categoria, Subcategoria, Match, Interes

class UsuarioSerializer(serializers.ModelSerializer):
    class Meta:
        model = Usuario
        # Solo incluir los campos que especificaste
        fields = [
            'id',
            'nombre',
            'apellido',
            'correo_electronico',
            'contrasena',  # Recuerda que esta contraseña debe estar hasheada antes de guardarse
            'genero',
            'foto_perfil',
            'direccion',
            'telefono',
            'pais',
            'ciudad',
            'fecha_nacimiento',
            'numero_identificacion',
            'es_empresa',
            'ultima_conexion',
            'fecha_creacion',
            'activo',
            'notificaciones'
        ]
        # Opcionalmente, podrías agregar 'extra_kwargs' para personalizar el comportamiento de ciertos campos
        extra_kwargs = {
            'contrasena': {'write_only': True}  # Evitar que la contraseña sea retornada en las respuestas
        }

class CategoriaSerializer(serializers.ModelSerializer):        
    class Meta:
        model = Categoria
        fields = '__all__'      

class SubcategoriaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Subcategoria
        fields = '__all__'

class MatchSerializer(serializers.ModelSerializer):
    class Meta:
        model = Match
        fields = '__all__'

class InteresSerializer(serializers.ModelSerializer):
    class Meta:
        model = Interes
        fields = '__all__'

class DocumentoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Documento
        fields = '__all__'
    
    # def validate_archivo(self, value):
    #     # Verifica si el archivo es un PDF
    #     if not value.name.endswith('.pdf'):
    #         raise serializers.ValidationError("Solo se permiten archivos PDF.")
    #     return value