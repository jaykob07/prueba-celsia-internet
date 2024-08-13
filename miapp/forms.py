from django import forms
from .models import Cliente, Servicio

class ClienteForm(forms.ModelForm):
    class Meta:
        model = Cliente
        fields = ['identificacion', 'nombres', 'apellidos', 'tipo_identificacion', 'fecha_nacimiento', 'numero_celular', 'correo_electronico']

class ServiciosForm(forms.ModelForm):
    class Meta:
        model = Servicio
        fields = ['identificacion', 'servicio', 'fechaInicio', 'ultimaFactura', 'ultimoPago']
