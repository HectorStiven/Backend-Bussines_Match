from rest_framework import generics
from .models import Documento, Usuario, Categoria, Subcategoria, Match, Interes    
from .serializer import DocumentoSerializer, UsuarioSerializer, CategoriaSerializer, SubcategoriaSerializer, MatchSerializer, InteresSerializer
from rest_framework.response import Response
from rest_framework import status
from rest_framework.exceptions import NotFound,ValidationError,PermissionDenied
from django.shortcuts import render
from rest_framework.permissions import IsAuthenticated  # Importar la clase de permisos

# Create your views here.


class ListarCategoria(generics.ListAPIView):    
    queryset = Categoria.objects.all()
    serializer_class = CategoriaSerializer

    def get(self, request, *args, **kwargs):
        queryset = self.filter_queryset(self.get_queryset())
        serializer = self.get_serializer(queryset, many=True)
        return Response({
            'success': True,
            'detail': 'Lista de categorias registradas',
            'data': serializer.data
        }, status=status.HTTP_200_OK)
    
class CrearCategoria(generics.CreateAPIView):
    queryset = Categoria.objects.all()
    serializer_class = CategoriaSerializer

    def post(self, request, *args, **kwargs):
        serializer = CategoriaSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({
                'success': True,
                'detail': 'Categoria creada exitosamente',
                'data': serializer.data
            }, status=status.HTTP_201_CREATED)
        else:
            return Response({
                'success': False,
                'detail': 'Error al crear la categoria',
                'data': serializer.errors
            }, status=status.HTTP_400_BAD_REQUEST)
        
class ActualizarCategoria(generics.UpdateAPIView):
    queryset = Categoria.objects.all()
    serializer_class = CategoriaSerializer

    def put(self, request, *args, **kwargs):
        instance = self.get_object()
        serializer = CategoriaSerializer(instance, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({
                'success': True,
                'detail': 'Categoria actualizada exitosamente',
                'data': serializer.data
            }, status=status.HTTP_200_OK)
        else:
            return Response({
                'success': False,
                'detail': 'Error al actualizar la categoria',
                'data': serializer.errors
            }, status=status.HTTP_400_BAD_REQUEST)
        
class EliminarCategoria(generics.DestroyAPIView):
    queryset = Categoria.objects.all()
    serializer_class = CategoriaSerializer

    def delete(self, request, *args, **kwargs):
        instance = self.get_object()
        self.perform_destroy(instance)
        return Response({
            'success': True,
            'detail': 'Categoria eliminada exitosamente',
            'data': []
        }, status=status.HTTP_204_NO_CONTENT)

class ListarSubcategoria(generics.ListAPIView):
    queryset = Subcategoria.objects.all()
    serializer_class = SubcategoriaSerializer

    def get(self, request, *args, **kwargs):
        queryset = self.filter_queryset(self.get_queryset())
        serializer = self.get_serializer(queryset, many=True)
        return Response({
            'success': True,
            'detail': 'Lista de subcategorias registradas',
            'data': serializer.data
        }, status=status.HTTP_200_OK)

class CrearSubcategoria(generics.CreateAPIView):
    queryset = Subcategoria.objects.all()
    serializer_class = SubcategoriaSerializer

    def post(self, request, *args, **kwargs):
        serializer = SubcategoriaSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({
                'success': True,
                'detail': 'Subcategoria creada exitosamente',
                'data': serializer.data
            }, status=status.HTTP_201_CREATED)
        else:
            return Response({
                'success': False,
                'detail': 'Error al crear la subcategoria',
                'data': serializer.errors
            }, status=status.HTTP_400_BAD_REQUEST)
        
class ActualizarSubcategoria(generics.UpdateAPIView):
    queryset = Subcategoria.objects.all()
    serializer_class = SubcategoriaSerializer

    def put(self, request, *args, **kwargs):
        instance = self.get_object()
        serializer = SubcategoriaSerializer(instance, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({
                'success': True,
                'detail': 'Subcategoria actualizada exitosamente',
                'data': serializer.data
            }, status=status.HTTP_200_OK)
        else:
            return Response({
                'success': False,
                'detail': 'Error al actualizar la subcategoria',
                'data': serializer.errors
            }, status=status.HTTP_400_BAD_REQUEST)
        


     
class EliminarSubcategoria(generics.DestroyAPIView):
    queryset = Subcategoria.objects.all()
    serializer_class = SubcategoriaSerializer

    def delete(self, request, *args, **kwargs):
        instance = self.get_object()
        self.perform_destroy(instance)
        return Response({
            'success': True,
            'detail': 'Categoria eliminada exitosamente',
            'data': []
        }, status=status.HTTP_204_NO_CONTENT)
    

class ListarMatch(generics.ListAPIView):
    queryset = Match.objects.all()
    serializer_class = MatchSerializer
    permission_classes = [IsAuthenticated]

    def get(self, request, *args, **kwargs):
        queryset = self.filter_queryset(self.get_queryset())
        serializer = self.get_serializer(queryset, many=True)
        return Response({
            'success': True,
            'detail': 'Lista de matches registrados',
            'data': serializer.data
        }, status=status.HTTP_200_OK)

class CrearMatch(generics.CreateAPIView):
    queryset = Match.objects.all()
    serializer_class = MatchSerializer

    def post(self, request, *args, **kwargs):
        serializer = MatchSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({
                'success': True,
                'detail': 'Match creado exitosamente',
                'data': serializer.data
            }, status=status.HTTP_201_CREATED)
        else:
            return Response({
                'success': False,
                'detail': 'Error al crear el match',
                'data': serializer.errors
            }, status=status.HTTP_400_BAD_REQUEST)
        

class ActualizarMatch(generics.UpdateAPIView):
    queryset = Match.objects.all()
    serializer_class = MatchSerializer

    def put(self, request, *args, **kwargs):
        instance = self.get_object()
        serializer = MatchSerializer(instance, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({
                'success': True,
                'detail': 'Match actualizado exitosamente',
                'data': serializer.data
            }, status=status.HTTP_200_OK)
        else:
            return Response({
                'success': False,
                'detail': 'Error al actualizar el match',
                'data': serializer.errors
            }, status=status.HTTP_400_BAD_REQUEST)
    
class EliminarMatch(generics.DestroyAPIView):
    queryset = Match.objects.all()
    serializer_class = MatchSerializer

    def delete(self, request, *args, **kwargs):
        instance = self.get_object()
        self.perform_destroy(instance)
        return Response({
            'success': True,
            'detail': 'Match eliminado exitosamente',
            'data': []
        }, status=status.HTTP_204_NO_CONTENT)
    
class ListarInteres(generics.ListAPIView):  
    queryset = Interes.objects.all()
    serializer_class = InteresSerializer

    def get(self, request, *args, **kwargs):
        queryset = self.filter_queryset(self.get_queryset())
        serializer = self.get_serializer(queryset, many=True)
        return Response({
            'success': True,
            'detail': 'Lista de intereses registrados',
            'data': serializer.data
        }, status=status.HTTP_200_OK)

class CrearInteres(generics.CreateAPIView):
    queryset = Interes.objects.all()
    serializer_class = InteresSerializer

    def post(self, request, *args, **kwargs):
        serializer = InteresSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({
                'success': True,
                'detail': 'Interes creado exitosamente',
                'data': serializer.data
            }, status=status.HTTP_201_CREATED)
        else:
            return Response({
                'success': False,
                'detail': 'Error al crear el interes',
                'data': serializer.errors
            }, status=status.HTTP_400_BAD_REQUEST)

class ActualizarInteres(generics.UpdateAPIView):
    queryset = Interes.objects.all()
    serializer_class = InteresSerializer

    def put(self, request, *args, **kwargs):
        instance = self.get_object()
        serializer = InteresSerializer(instance, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({
                'success': True,
                'detail': 'Interes actualizado exitosamente',
                'data': serializer.data
            }, status=status.HTTP_200_OK)
        else:
            return Response({
                'success': False,
                'detail': 'Error al actualizar el interes',
                'data': serializer.errors
            }, status=status.HTTP_400_BAD_REQUEST)

class EliminarInteres(generics.DestroyAPIView):
    queryset = Interes.objects.all()
    serializer_class = InteresSerializer

    def delete(self, request, *args, **kwargs):
        instance = self.get_object()
        self.perform_destroy(instance)
        return Response({
            'success': True,
            'detail': 'Interes eliminado exitosamente',
            'data': []
        }, status=status.HTTP_204_NO_CONTENT)
    

class SubirDocumentos(generics.CreateAPIView):
    queryset = Documento.objects.all()
    serializer_class = DocumentoSerializer

    def post(self, request, *args, **kwargs):
        serializer = DocumentoSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({
                'success': True,
                'detail': 'Documento subido exitosamente',
                'data': serializer.data
            }, status=status.HTTP_201_CREATED)
        else:
            return Response({
                'success': False,
                'detail': 'Error al subir el documento',
                'data': serializer.errors
            }, status=status.HTTP_400_BAD_REQUEST)
        
        
class ListarDocumentos(generics.ListAPIView):
    queryset = Documento.objects.all()
    serializer_class = DocumentoSerializer

    def get(self, request, *args, **kwargs):
        queryset = self.filter_queryset(self.get_queryset())
        serializer = self.get_serializer(queryset, many=True)
        return Response({
            'success': True,
            'detail': 'Lista de documentos registrados',
            'data': serializer.data
        }, status=status.HTTP_200_OK)