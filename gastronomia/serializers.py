from .models import Establecimiento
from rest_framework import serializers

class EstablecimientoSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Establecimiento
        fields = ['nombre',
            'fecha',
            'ruc',
            'parroquia',
            'sector',
            'telefono',
            'email',
            'propietario',
            'tipo',
            'redes_sociales',
            'asociacion',
            'local',
            'equipos',
            'equipos_cocina',
            'servicios_complementarios',
            'numero_mesas',
            'plazas',
            'banio',
            'oferta',
            'tipo_servicio',
            'menu',
            'precio_promedio',
            'proceso',
            'materias_primas',
            'tipo_materia_prima',
            'numero_mujeres',
            'numero_hombres',
            'formacion_academica',
            'personal_capacitado',
            'frecuencia_capacitacion',
            'empleados_formacion',
            'licencia_anual',
            'url',
            'latitude',
            'longitude'
            ]

class NombreSerializer(serializers.Serializer):
    nombre = serializers.CharField()
