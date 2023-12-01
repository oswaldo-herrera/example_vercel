from django.urls import path
from django.conf import settings
from django.conf.urls.static import static

from . import views

app_name = 'user_app'


urlpatterns = [
    path('registro/', views.RegistrarUsuario.as_view(), name='registro'),
    path('lista-usuarios/',views.ListaUsuarios.as_view(),name='lista_usuarios'),
    path('eliminar-usuarios/<int:pk>/',views.EliminarUsuarios.as_view(),name='eliminar_usuarios'),
    path('editar-usuarios/<int:pk>/',views.EditarUsuario.as_view(),name='editar_usuarios'),
]
