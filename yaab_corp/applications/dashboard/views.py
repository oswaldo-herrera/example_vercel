from django.shortcuts import render
from django.views import View
from django.views.generic import TemplateView
from django.views.generic import ListView,UpdateView,CreateView,DeleteView
from django.http import HttpResponse, HttpResponseRedirect, JsonResponse
from django.shortcuts import render,redirect,get_object_or_404

from django.urls import reverse_lazy,reverse
from django.template.loader import get_template

from .models import Productos,Plazo,Simulador
from .forms import ProductosForm,PlazoPagoForm,SimuladorForm

from applications.users.models import User
from applications.users.forms import UserChangeForm

# Create your views here.from django.views.generic.base import TemplateView

class DashboardView(CreateView):
    template_name="dashboard/index.html"
    form_class = SimuladorForm
    success_url = reverse_lazy('dashboard_app:index')
    
    def get_context_data(self, **kwargs):
        context = super(DashboardView, self).get_context_data(**kwargs)
        user = self.kwargs.get('pk')
        # context['usuario_id'] = User.objects.filter(id = user)
        context['pk'] = user
        context['simula'] = Simulador.objects.filter(id=user)
        # context['usuarios'] = User.objects.all()

        return context
    
    def form_valid(self, form):
        tipo_credito = form.cleaned_data['tipo_credito']
        plazo_nombre = form.cleaned_data['plazo_nombre']
        amount = form.cleaned_data['amount']
        interest_rate = form.cleaned_data['interest_rate']
        term = form.cleaned_data['term']

        # Realiza el cálculo
        monthly_interest_rate = (interest_rate / 12) / 100
        num_payments = term * 12
        monthly_payment = (amount * monthly_interest_rate) / (1 - (1 + monthly_interest_rate) ** -num_payments) + + + (amount / 12) 

        # Guarda los resultados en la base de datos o donde lo necesites
        # Aquí se asume que hay un modelo Loan para guardar los resultados
        loan = Simulador(amount=amount, tipo_credito = tipo_credito,plazo_nombre=plazo_nombre, interest_rate=interest_rate, term=term, monthly_payment=monthly_payment)
        loan.save()

        # return redirect('panel_app:panel_index')
        # return render(self.request,'panel/index.html', {'form': form, 'monthly_payment': monthly_payment})
        response_data = {'monthly_payment': monthly_payment}
        return JsonResponse(response_data)

def obtener_interes(request):
    if request.method == 'GET':
        product_id = request.GET.get('product_id')
        try:
            plazo = Plazo.objects.get(id=product_id)
            interest = plazo.interes_credito
            return JsonResponse({'interest': interest})
        except Productos.DoesNotExist:
            return JsonResponse({'interest': None})
        
def obtener_plazo(request):
    if request.method == 'GET':
        product_id = request.GET.get('product_id')
        try:
            product = Plazo.objects.get(id=product_id)
            plazo = product.semanas
            return JsonResponse({'plazo': plazo})
        except Productos.DoesNotExist:
            return JsonResponse({'plazo': None})
          


class PreguntasRespuestas(TemplateView):
    template_name = 'dashboard/preguntas-respuestas.html'
 
 
class ProductosView(ListView):
    model = Productos
    template_name = 'dashboard/productos/productos.html'
    context_object_name = 'productos'
    
    def get_queryset(self):
        producto = Productos.objects.all()
        return  producto
    
    def get_context_data(self, **kwargs):
        context = super(ProductosView,self).get_context_data(**kwargs)
        
        context["plazo"] = Plazo.objects.all()  
        
        return context
        

        
    
#####productos#####
    
class CreateProductosView(CreateView):
    model=Productos
    form_class = ProductosForm
    template_name = 'dashboard/productos/nuevo-producto.html'
    success_url = reverse_lazy('dashboard_app:productos_gral')

class EditarProducto(UpdateView):
    model = Productos
    template_name = 'dashboard/productos/editar-productos.html'
    form_class = ProductosForm
    success_url = reverse_lazy('dashboard_app:productos_gral')  
    
class EliminarProducto(DeleteView):
    model = Productos
    template_name = 'dashboard/productos/eliminar-productos.html'
    form_class = ProductosForm
    success_url = reverse_lazy('dashboard_app:productos_gral') 

#####productos#####

#####plazo#####

class CreatePlazoView(CreateView):
    model = Plazo
    form_class = PlazoPagoForm
    template_name = 'dashboard/plazos/nuevo-plazo.html'
    success_url = reverse_lazy('dashboard_app:productos_gral')
    
class EditarPlazoView(UpdateView):
    model = Plazo
    form_class = PlazoPagoForm
    template_name = 'dashboard/plazos/editar-plazo.html'
    success_url = reverse_lazy('dashboard_app:productos_gral') 

class EliminarPlazo(DeleteView):
    model = Plazo
    template_name = 'dashboard/plazos/eliminar-plazo.html'
    form_class = PlazoPagoForm
    success_url = reverse_lazy('dashboard_app:productos_gral') 
    
#####plazo#####


class EditarUsuarioUsers(UpdateView):
    model = User
    template_name = 'dashboard/registro-usuario/completar-registro.html'
    form_class = UserChangeForm
    success_url = reverse_lazy('dashboard_app:index')
    
class TerminosCondiciones(TemplateView):
    template_name = 'dashboard/terminos-condiciones.html'
