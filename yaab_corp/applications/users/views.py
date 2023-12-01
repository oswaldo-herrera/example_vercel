from django.shortcuts import render
from django.urls import reverse_lazy
from django.contrib.auth import get_user_model
from django.contrib.auth.hashers import make_password
from django.views.generic import View,TemplateView,ListView,UpdateView,CreateView,DeleteView
from .models import User
from .forms import UserCreationForm,UserChangeForm
# Create your views here.

class RegistrarUsuario(CreateView):
    model = User
    template_name = 'users/register.html'
    form_class = UserCreationForm
    success_url = reverse_lazy('login')
    
    def form_valid(self, form):
        # Obtenemos los datos del formulario
        email = form.cleaned_data['email']
        password = form.cleaned_data['password1']  # Obtenemos la contraseña

        # Creamos una instancia del modelo de usuario pero no la guardamos aún
        user = form.save(commit=False)
        # Usamos make_password para cifrar la contraseña antes de guardarla
        user.password = make_password(password)
        user.save()
        return super().form_valid(form)
    
    
class EditarUsuario(UpdateView):
    model = User
    template_name = 'users/editar-usuario.html'
    form_class = UserChangeForm
    success_url = reverse_lazy('user_app:lista_usuarios')

class EliminarUsuarios(DeleteView):
    model = User
    template_name = 'users/eliminar-usuario.html'
    # form_class = CreateUserForm
    success_url = reverse_lazy('user_app:lista_usuarios')
    
class ListaUsuarios(ListView):
    # model = User
    template_name = 'users/listar-usuarios.html'
    context_object_name = 'lista'

    def get_queryset(self):
        listar = User.objects.all()
        return listar
