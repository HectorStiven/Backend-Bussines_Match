from Bussines_central.login import login as login
from . import views as viwes

from django.urls import path

urlpatterns = [
    path('listar_usuario/', login.ListarUsuario.as_view(), name='listar_usuario'),
    path('crear_usuario/', login.CrearUsuario.as_view(), name='crear_usuario'),
    path('actualizar_usuario/<int:pk>/', login.ActualizarUsuario.as_view(), name='actualizar_usuario'),
    path('eliminar_usuario/<int:pk>/', login.EliminarUsuario.as_view(), name='eliminar_usuario'),

    path('LoginUsuario/', login.LoginUsuario.as_view(), name='listar_categoria'),

   path('listar_categoria/', viwes.ListarCategoria.as_view(), name='listar_categoria'),
    path('crear_categoria/', viwes.CrearCategoria.as_view(), name='crear_categoria'),
    path('actualizar_categoria/<int:pk>/', viwes.ActualizarCategoria.as_view(), name='actualizar_categoria'),
    path('eliminar_categoria/<int:pk>/', viwes.EliminarCategoria.as_view(), name='eliminar_categoria'),

   path('listar_subcategoria/', viwes.ListarSubcategoria.as_view(), name='listar_subcategoria'),
    path('crear_subcategoria/', viwes.CrearSubcategoria.as_view(), name='crear_subcategoria'),
    path('actualizar_subcategoria/<int:pk>/', viwes.ActualizarSubcategoria.as_view(), name='actualizar_subcategoria'),
    path('eliminar_subcategoria/<int:pk>/', viwes.EliminarSubcategoria.as_view(), name='eliminar_subcategoria'),

    path('listar_match/', viwes.ListarMatch.as_view(), name='listar_match'),
    path('crear_match/', viwes.CrearMatch.as_view(), name='crear_match'),
    path('actualizar_match/<int:pk>/', viwes.ActualizarMatch.as_view(), name='actualizar_match'),
    path('eliminar_match/<int:pk>/', viwes.EliminarMatch.as_view(), name='eliminar_match'),



]