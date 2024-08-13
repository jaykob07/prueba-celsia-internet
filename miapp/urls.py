from django.urls import path
from . import views
from .views import ClienteListView, ClienteCreateView, ServicioListView, ServicioCreateView, home

urlpatterns = [
    path('', home, name='home'),  
    path('clientes/', ClienteListView.as_view(), name='clientes_list'),
    path('clientes/create/', ClienteCreateView.as_view(), name='cliente_create'),
    path('servicios/', ServicioListView.as_view(), name='servicios_list'),
    path('servicios/create/', ServicioCreateView.as_view(), name='servicio_create'),
]