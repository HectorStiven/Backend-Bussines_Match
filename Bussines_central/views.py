from rest_framework import generics
from .models import Documento, Usuario, Categoria, Subcategoria, Match, Interes    
from .serializer import DocumentoSerializer, MatchSerializerCrear, UsuarioSerializer, CategoriaSerializer, SubcategoriaSerializer, MatchSerializer, InteresSerializer,MatchSerializerSave
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
    
class ListarMatchPorUsuario(generics.ListAPIView):
    serializer_class = MatchSerializer

    def get_queryset(self):
        # Obtener el id de usuario desde los parámetros de la URL
        usuario_id = self.kwargs['usuario_id']
        
        # Filtrar los registros de Match para el usuario dado
        queryset = Match.objects.filter(usuario_id=usuario_id)
        
        # Si no se encuentran registros, devolvemos un queryset vacío
        if not queryset.exists():
            return Match.objects.none()  # No devuelve nada si no hay coincidencias
        
        return queryset

    def get(self, request, *args, **kwargs):
        # Llamamos a la lógica de `get_queryset` para obtener los matches filtrados
        queryset = self.get_queryset()
        # Serializamos los datos
        serializer = self.get_serializer(queryset, many=True)
        
        # Retornamos la respuesta con los datos serializados
        return Response({
            'success': True,
            'detail': 'Lista de matches encontrados para el usuario',
            'data': serializer.data
        }, status=status.HTTP_200_OK)
    
    
class CrearMatch(generics.CreateAPIView):
    queryset = Match.objects.all()
    serializer_class = MatchSerializerCrear

    def post(self, request, *args, **kwargs):
        serializer = MatchSerializerCrear(data=request.data)
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
    serializer_class = MatchSerializerSave

    def update(self, request, *args, **kwargs):
        partial = kwargs.pop('partial', False)
        instance = self.get_object()
        serializer = self.get_serializer(instance, data=request.data, partial=partial)
        
        if serializer.is_valid():
            self.perform_update(serializer)
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

class ActualizarNumerosSugeridos(generics.UpdateAPIView):
    def put(self, request, pk, *args, **kwargs):
        # Obtener el objeto Match según el ID
        try:
            match = Match.objects.get(pk=pk)
        except Match.DoesNotExist:
            return Response({
                'success': False,
                'detail': 'Match no encontrado'
            }, status=status.HTTP_404_NOT_FOUND)
        
        # Obtener el número y el valor de 'activo' desde la solicitud
        numero = request.data.get("numero")
        activo = request.data.get("activo")
        
        if numero is None:
            return Response({
                'success': False,
                'detail': 'Se requiere un número en la solicitud'
            }, status=status.HTTP_400_BAD_REQUEST)
        
        # Agregar el número al arreglo de numeros_sugeridos
        match.numeros_sugeridos.append(numero)

        # Si 'activo' se ha proporcionado, actualizar el estado
        if activo is not None:
            match.activo = activo
        
        # Guardar el objeto después de las actualizaciones
        match.save()
        
        # Serializar los datos y responder con éxito
        serializer = MatchSerializer(match)
        return Response({
            'success': True,
            'detail': 'Número y estado activo actualizados exitosamente',
            'data': serializer.data
        }, status=status.HTTP_200_OK)
    
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