from django.shortcuts import render
from .models import Cliente, Servicio
from django.shortcuts import render, redirect
from django.views.generic import ListView, CreateView
from django.urls import reverse_lazy


def home(request):
    return render(request, 'miapp/home.html')


class ClienteListView(ListView):
    model = Cliente
    template_name = 'miapp/clientes_list.html'  # Nombre del template HTML
    context_object_name = 'clientes'

class ServicioListView(ListView):
    model = Servicio
    template_name = 'miapp/servicios_list.html'
    context_object_name = 'servicios'


class ClienteCreateView(CreateView):
    model = Cliente
    fields = ['identificacion', 'nombres', 'apellidos', 'tipo_identificacion', 'fecha_nacimiento', 'numero_celular', 'correo_electronico']
    template_name = 'miapp/cliente_form.html'
    success_url = reverse_lazy('clientes_list')  # Redirige a la lista de clientes

class ServicioCreateView(CreateView):
    model = Servicio
    fields = ['identificacion', 'servicio', 'fecha_inicio', 'ultima_facturacion', 'ultimo_pago']
    template_name = 'miapp/servicio_form.html'
    success_url = reverse_lazy('servicios_list')  # Redirige a la lista de servicios