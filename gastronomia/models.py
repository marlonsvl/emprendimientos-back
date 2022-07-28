from django.db import models

## https://stackoverflow.com/questions/19130942/whats-the-best-way-to-store-a-phone-number-in-django-models
#from phonenumber_field.modelfields import PhoneNumberField

# Create your models here.

class Establecimiento(models.Model):
    ACTIVE_CHOICES = [
        ("Si", "Si"),
        ("No", "No")
    ]
    nombre = models.CharField(max_length=200)
    fecha = models.DateTimeField('fecha')
    ruc = models.CharField(max_length=2, choices=ACTIVE_CHOICES)
    parroquia = models.CharField(max_length=100)
    sector = models.CharField(max_length=200)
    telefono = models.CharField(max_length=20)
    email = models.EmailField(max_length=254)
    propietario = models.CharField(max_length=200)
    tipo = models.CharField(max_length=100) # col 17
    redes_sociales = models.CharField(max_length=100)
    asociacion = models.CharField(max_length=200)
    local = models.CharField(max_length=200)
    equipos = models.CharField(max_length=500)
    equipos_cocina = models.CharField(max_length=500)
    servicios_complementarios = models.CharField(max_length=500)
    numero_mesas = models.IntegerField()
    plazas = models.IntegerField()
    banio = models.CharField(max_length=2, choices=ACTIVE_CHOICES)
    oferta = models.CharField(max_length=200)
    tipo_servicio = models.CharField(max_length=200)
    menu = models.TextField(max_length=1200, null=True)
    precio_promedio = models.DecimalField(
        decimal_places=2, max_digits=10)
    proceso = models.CharField(max_length=200) # 25
    materias_primas = models.CharField(max_length=200) # 26
    tipo_materia_prima = models.CharField(max_length=200) # 27
    numero_mujeres = models.IntegerField() # 28
    numero_hombres = models.IntegerField() # 29
    formacion_academica = models.CharField(max_length=200) # 30
    personal_capacitado = models.CharField(max_length=2, choices=ACTIVE_CHOICES) #31
    frecuencia_capacitacion = models.CharField(max_length=200) # 32
    empleados_formacion = models.CharField(max_length=200) # 33
    licencia_anual = models.CharField(max_length=2, choices=ACTIVE_CHOICES) #35
    url = models.URLField(null=True, blank=True, max_length=250)
    latitude = models.DecimalField(max_digits=9, decimal_places=6) # y
    longitude = models.DecimalField(max_digits=9, decimal_places=6) # x

    def __str__(self):
        return f"Nombre: {self.nombre}, Fecha: {self.fecha}, Parroquia: {self.parroquia}"


