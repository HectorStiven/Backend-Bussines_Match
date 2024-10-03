from rest_framework import serializers
from .models import Usuario, Categoria, Subcategoria, Match, Interes
from django.contrib.auth.hashers import make_password





class UsuarioSerializer(serializers.ModelSerializer):
    class Meta:
        model = Usuario
        fields = '__all__'

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