from rest_framework import generics

from rest_framework.response import Response
from rest_framework import status

from Bussines_central.models import Usuario
from Bussines_central.serializer import UsuarioSerializer

from rest_framework.permissions import IsAuthenticated  # Importar la clase de permisos

from rest_framework_simplejwt.tokens import RefreshToken
from django.contrib.auth.hashers import check_password,make_password


from django.contrib.auth.hashers import make_password
from rest_framework.permissions import AllowAny




class CrearUsuario(generics.CreateAPIView):
    queryset = Usuario.objects.all()
    serializer_class = UsuarioSerializer
    permission_classes = [AllowAny]  # Permitir a cualquier usuario crear una cuenta

    def perform_create(self, serializer):
        contrasena = serializer.validated_data.get('contrasena')
        if contrasena:
            # Hashear la contraseña
            serializer.validated_data['contrasena'] = make_password(contrasena)  
        serializer.save()

    def post(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        
        # Verificar si el correo electrónico o número de identificación ya existen
        if Usuario.objects.filter(correo_electronico=request.data.get('correo_electronico')).exists():
            return Response({
                'success': False,
                'detail': 'El correo electrónico ya está en uso.',
            }, status=status.HTTP_400_BAD_REQUEST)

        if Usuario.objects.filter(numero_identificacion=request.data.get('numero_identificacion')).exists():
            return Response({
                'success': False,
                'detail': 'El número de identificación ya está en uso.',
            }, status=status.HTTP_400_BAD_REQUEST)

        # Validar el serializer
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)  # Llama al método para guardar el usuario

        return Response({
            'success': True,
            'detail': 'Usuario creado exitosamente',
            'data': serializer.data
        }, status=status.HTTP_201_CREATED)
        




class ActualizarUsuario(generics.UpdateAPIView):
    queryset = Usuario.objects.all()
    serializer_class = UsuarioSerializer

    def put(self, request, *args, **kwargs):
        instance = self.get_object()
        serializer = UsuarioSerializer(instance, data=request.data)

        if serializer.is_valid():
            # Verifica si se está actualizando la contraseña
            if 'contrasena' in request.data:
                contrasena = request.data['contrasena']
                hashed_password = make_password(contrasena)
                # Asegúrate de guardar la contraseña hasheada
                serializer.save(contrasena=hashed_password)
            else:
                # Si no se actualiza la contraseña, guarda el resto de los datos
                serializer.save()

            return Response({
                'success': True,
                'detail': 'Usuario actualizado exitosamente',
                'data': serializer.data
            }, status=status.HTTP_200_OK)
        else:
            return Response({
                'success': False,
                'detail': 'Error al actualizar el usuario',
                'data': serializer.errors
            }, status=status.HTTP_400_BAD_REQUEST)
        

        

class EliminarUsuario(generics.DestroyAPIView):
    queryset = Usuario.objects.all()
    serializer_class = UsuarioSerializer

    def delete(self, request, *args, **kwargs):
        instance = self.get_object()
        self.perform_destroy(instance)
        return Response({
            'success': True,
            'detail': 'Usuario eliminado exitosamente',
            'data': []
        }, status=status.HTTP_204_NO_CONTENT)
    




class ListarUsuario(generics.GenericAPIView):
    serializer_class = UsuarioSerializer
    permission_classes = [IsAuthenticated]  # Asegúrate de que se requiera autenticación

    def get(self, request, pk, *args, **kwargs):
        try:
            # Obtener el objeto Usuario según el ID proporcionado en la URL
            usuario = Usuario.objects.get(pk=pk)
        except Usuario.DoesNotExist:
            return Response({
                'success': False,
                'detail': 'Usuario no encontrado'
            }, status=status.HTTP_404_NOT_FOUND)

        # Serializar el usuario encontrado
        serializer = self.get_serializer(usuario)

        # Devolver la respuesta con el usuario encontrado
        return Response({
            'success': True,
            'detail': 'Usuario encontrado',
            'data': serializer.data
        }, status=status.HTTP_200_OK)

class LoginUsuario(generics.GenericAPIView):
    serializer_class = UsuarioSerializer
    permission_classes = [AllowAny]  # Permitir acceso a cualquier usuario sin autenticación

    def post(self, request, *args, **kwargs):
        numero_identificacion = request.data.get('numero_identificacion')
        contrasena = request.data.get('contrasena')

        # Validar campos vacíos
        if not numero_identificacion or not contrasena:
            return Response({
                'success': False,
                'detail': 'Número de identificación y contraseña son requeridos.'
            }, status=status.HTTP_400_BAD_REQUEST)

        # Buscar usuario por número de identificación
        try:
            usuario = Usuario.objects.get(numero_identificacion=numero_identificacion)
        except Usuario.DoesNotExist:
            return Response({
                'success': False,
                'detail': 'Usuario no encontrado.'
            }, status=status.HTTP_404_NOT_FOUND)

        # Comparar contraseñas usando check_password
        if check_password(contrasena, usuario.contrasena):
            # Generar tokens JWT usando RefreshToken
            refresh = RefreshToken.for_user(usuario)
            access_token = refresh.access_token

            return Response({
                'success': True,
                'detail': 'Login exitoso.',
                'access_token': str(access_token),  # Token de acceso
                'refresh_token': str(refresh),  # Token de refresco
                'data': UsuarioSerializer(usuario).data
            }, status=status.HTTP_200_OK)
        else:
            return Response({
                'success': False,
                'detail': 'Contraseña incorrecta.'
            }, status=status.HTTP_400_BAD_REQUEST)
        
