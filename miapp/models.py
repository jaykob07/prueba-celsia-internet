from django.db import models


class Cliente(models.Model):
    identificacion = models.CharField(max_length=20, primary_key=True)
    nombres = models.CharField(max_length=80)
    apellidos = models.CharField(max_length=80)
    tipo_identificacion = models.CharField(max_length=2)
    fecha_nacimiento = models.DateField()
    numero_celular = models.CharField(max_length=20)
    correo_electronico = models.EmailField(max_length=80)

    def __str__(self):
        return f"{self.nombres} {self.apellidos}"

class Servicio(models.Model):
    identificacion = models.ForeignKey(Cliente, on_delete=models.CASCADE)
    servicio = models.CharField(max_length=80)
    fecha_inicio = models.DateField()
    ultima_facturacion = models.DateField()
    ultimo_pago = models.IntegerField(default=0)

    class Meta:
        unique_together = ('identificacion', 'servicio')

    def __str__(self):
        return f"{self.servicio} for {self.identificacion}"
