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
            serializer.validated_data['contrasena'] = make_password(contrasena)  # Hashearla si no se maneja automáticamente
        serializer.save()

    def post(self, request, *args, **kwargs):
        serializer = UsuarioSerializer(data=request.data)
        if serializer.is_valid():
            self.perform_create(serializer)  # Llama al método para guardar el usuario
            return Response({
                'success': True,
                'detail': 'Usuario creado exitosamente',
                'data': serializer.data
            }, status=status.HTTP_201_CREATED)
        else:
            return Response({
                'success': False,
                'detail': 'Error al crear el usuario',
                'data': serializer.errors
            }, status=status.HTTP_400_BAD_REQUEST)
        
# class CrearUsuario(generics.CreateAPIView):
#     queryset = Usuario.objects.all()
#     serializer_class = UsuarioSerializer
#     permission_classes = [AllowAny]  # Permitir a cualquier usuario crear una cuenta

#     def perform_create(self, serializer):
#         contrasena = serializer.validated_data.get('contrasena')
#         if contrasena:
#             serializer.validated_data['contrasena'] = make_password(contrasena)  # Hashearla si no se maneja automáticamente
#         serializer.save()

#     def post(self, request, *args, **kwargs):
#         serializer = UsuarioSerializer(data=request.data)
#         if serializer.is_valid():
#             self.perform_create(serializer)  # Llama al método para guardar el usuario
#             return Response({
#                 'success': True,
#                 'detail': 'Usuario creado exitosamente',
#                 'data': serializer.data
#             }, status=status.HTTP_201_CREATED)
#         else:
#             return Response({
#                 'success': False,
#                 'detail': 'Error al crear el usuario',
#                 'data': serializer.errors
#             }, status=status.HTTP_400_BAD_REQUEST)
        
# class CrearUsuario(generics.CreateAPIView):
#     queryset = Usuario.objects.all()
#     serializer_class = UsuarioSerializer
#     permission_classes = [AllowAny]  # Permitir a cualquier usuario crear una cuenta

#     def perform_create(self, serializer):
#         # Verifica si el serializer se encarga de hashear la contraseña
#         contrasena = serializer.validated_data.get('contrasena')
#         if contrasena:
#             serializer.validated_data['contrasena'] = make_password(contrasena)  # Hashearla si no se maneja automáticamente
#         serializer.save()

#     def post(self, request, *args, **kwargs):
#         serializer = UsuarioSerializer(data=request.data)
#         if serializer.is_valid():
#             self.perform_create(serializer)  # Llama al método para guardar el usuario
#             return Response({
#                 'success': True,
#                 'detail': 'Usuario creado exitosamente',
#                 'data': serializer.data
#             }, status=status.HTTP_201_CREATED)
#         else:
#             return Response({
#                 'success': False,
#                 'detail': 'Error al crear el usuario',
#                 'data': serializer.errors
#             }, status=status.HTTP_400_BAD_REQUEST)

# class CrearUsuario(generics.CreateAPIView):
#     queryset = Usuario.objects.all()
#     serializer_class = UsuarioSerializer
#     permission_classes = [IsAuthenticated]  # Asegúrate de que se requiera autenticación

#     def perform_create(self, serializer):
#         # Al crear el usuario, asegúrate de hashear la contraseña
#         contrasena = serializer.validated_data.get('contrasena')
#         hashed_password = make_password(contrasena)
#         serializer.save(contrasena=hashed_password)  # Guardar la contraseña hasheada

#     def post(self, request, *args, **kwargs):
#         serializer = UsuarioSerializer(data=request.data)
#         if serializer.is_valid():
#             self.perform_create(serializer)  # Llama al método para guardar el usuario
#             return Response({
#                 'success': True,
#                 'detail': 'Usuario creado exitosamente',
#                 'data': serializer.data
#             }, status=status.HTTP_201_CREATED)
#         else:
#             return Response({
#                 'success': False,
#                 'detail': 'Error al crear el usuario',
#                 'data': serializer.errors
#             }, status=status.HTTP_400_BAD_REQUEST)
        


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
    



# class ListarUsuario(generics.ListAPIView):
#     queryset = Usuario.objects.all()
#     serializer_class = UsuarioSerializer
#     permission_classes = [IsAuthenticated]

#     def get(self, request, *args, **kwargs):
#         try:
#             # Intenta validar el token
#             token = request.headers.get('Authorization').split()[1]
#             print(f"Token recibido: {token}")
#         except (IndexError, AttributeError):
#             print("Error al recibir el token")

#         queryset = self.filter_queryset(self.get_queryset())
#         serializer = self.get_serializer(queryset, many=True)
#         return Response({
#             'success': True,
#             'detail': 'Lista de personas registradas',
#             'data': serializer.data
#         }, status=status.HTTP_200_OK)
    

# class ListarUsuario(generics.ListAPIView):
#     queryset = Usuario.objects.all()
#     serializer_class = UsuarioSerializer

#     def get(self, request, *args, **kwargs):
#         queryset = self.filter_queryset(self.get_queryset())
#         serializer = self.get_serializer(queryset, many=True)
#         return Response({
#             'success': True,
#             'detail': 'Lista de personas registradas',
#             'data': serializer.data
#         }, status=status.HTTP_200_OK)
# class ListarUsuario(generics.ListAPIView):
#     queryset = Usuario.objects.all()
#     serializer_class = UsuarioSerializer
#     permission_classes = [IsAuthenticated]  # Asegúrate de que se requiera autenticación

#     def get(self, request, *args, **kwargs):
#         queryset = self.filter_queryset(self.get_queryset())
#         serializer = self.get_serializer(queryset, many=True)
#         return Response({
#             'success': True,
#             'detail': 'Lista de personas registradas',
#             'data': serializer.data
#         }, status=status.HTTP_200_OK)

# class ListarUsuario(generics.ListAPIView):
#     queryset = Usuario.objects.all()
#     serializer_class = UsuarioSerializer
#     permission_classes = [IsAuthenticated]  # Asegúrate de que se requiera autenticación

#     def get(self, request, *args, **kwargs):
#         queryset = self.filter_queryset(self.get_queryset())
#         serializer = self.get_serializer(queryset, many=True)
#         return Response({
#             'success': True,
#             'detail': 'Lista de personas registradas',
#             # 'data': serializer.data
#           }, status=status.HTTP_200_OK)
    

# class LoginUsuario(generics.GenericAPIView):
#     serializer_class = UsuarioSerializer
#     permission_classes = [AllowAny]  # Permitir acceso a cualquier usuario sin autenticación

#     def post(self, request, *args, **kwargs):
#         numero_identificacion = request.data.get('numero_identificacion')
#         contrasena = request.data.get('contrasena')

#         # Validar campos vacíos
#         if not numero_identificacion or not contrasena:
#             return Response({
#                 'success': False,
#                 'detail': 'Número de identificación y contraseña son requeridos.'
#             }, status=status.HTTP_400_BAD_REQUEST)

#         # Buscar usuario por número de identificación
#         try:
#             usuario = Usuario.objects.get(numero_identificacion=numero_identificacion)
#         except Usuario.DoesNotExist:
#             return Response({
#                 'success': False,
#                 'detail': 'Usuario no encontrado.'
#             }, status=status.HTTP_404_NOT_FOUND)

#         # Comparar contraseñas usando check_password
#         if check_password(contrasena, usuario.contrasena):
#             # Generar tokens JWT usando RefreshToken
#             refresh = RefreshToken.for_user(usuario)
#             access_token = refresh.access_token

#             return Response({
#                 'success': True,
#                 'detail': 'Login exitoso.',
#                 'access_token': str(access_token),  # Token de acceso
#                 'refresh_token': str(refresh),  # Token de refresco
#             }, status=status.HTTP_200_OK)
#         else:
#             return Response({
#                 'success': False,
#                 'detail': 'Contraseña incorrecta.'
#             }, status=status.HTTP_400_BAD_REQUEST)

from django.contrib.auth import authenticate

# class LoginUsuario(generics.GenericAPIView):
#     serializer_class = UsuarioSerializer
#     permission_classes = [AllowAny]  # Permitir acceso a cualquier usuario sin autenticación

#     def post(self, request, *args, **kwargs):
#         numero_identificacion = request.data.get('numero_identificacion')
#         password = request.data.get('password')

#         user = authenticate(request, username=numero_identificacion, password=password)

#         if user is not None:
#             refresh = RefreshToken.for_user(user)
#             return Response({
#                 'success': True,
#                 'refresh': str(refresh),
#                 'access': str(refresh.access_token),
#             }, status=status.HTTP_200_OK)
#         else:
#             return Response({
#                 'success': False,
#                 'detail': 'Credenciales inválidas'
#             }, status=status.HTTP_401_UNAUTHORIZED)


class ListarUsuario(generics.ListAPIView):
    queryset = Usuario.objects.all()
    serializer_class = UsuarioSerializer
    permission_classes = [IsAuthenticated]  # Asegúrate de que se requiera autenticación

    def get(self, request, *args, **kwargs):
        queryset = self.filter_queryset(self.get_queryset())
        serializer = self.get_serializer(queryset, many=True)
        return Response({
            'success': True,
            'detail': 'Lista de personas registradas',
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
            }, status=status.HTTP_200_OK)
        else:
            return Response({
                'success': False,
                'detail': 'Contraseña incorrecta.'
            }, status=status.HTTP_400_BAD_REQUEST)
        
# class LoginUsuario(generics.GenericAPIView):
#     serializer_class = UsuarioSerializer
#     permission_classes = [AllowAny]  # Permitir acceso a cualquier usuario sin autenticación

#     def post(self, request, *args, **kwargs):
#         numero_identificacion = request.data.get('numero_identificacion')
#         contrasena = request.data.get('contrasena')

#         # Validar campos vacíos
#         if not numero_identificacion or not contrasena:
#             return Response({
#                 'success': False,
#                 'detail': 'Número de identificación y contraseña son requeridos.'
#             }, status=status.HTTP_400_BAD_REQUEST)

#         # Buscar usuario por número de identificación
#         try:
#             usuario = Usuario.objects.get(numero_identificacion=numero_identificacion)
#         except Usuario.DoesNotExist:
#             return Response({
#                 'success': False,
#                 'detail': 'Usuario no encontrado.'
#             }, status=status.HTTP_404_NOT_FOUND)

#         # Comparar contraseñas usando check_password
#         if check_password(contrasena, usuario.contrasena):
#             # Generar tokens JWT usando RefreshToken
#             refresh = RefreshToken.for_user(usuario)
#             access_token = refresh.access_token

#             return Response({
#                 'success': True,
#                 'detail': 'Login exitoso.',
#                 'access_token': str(access_token),  # Token de acceso
#                 'refresh_token': str(refresh),  # Token de refresco
#             }, status=status.HTTP_200_OK)
#         else:
#             return Response({
#                 'success': False,
#                 'detail': 'Contraseña incorrecta.'
#             }, status=status.HTTP_400_BAD_REQUEST)