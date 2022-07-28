from tokenize import String
from django.shortcuts import render
from .models import Establecimiento
from .serializers import EstablecimientoSerializer, NombreSerializer
from rest_framework import viewsets
from rest_framework import generics

# Create your views here.
#from django.http import HttpResponse

PARROQUIAS = {"Taquil": "Taquil",
            "Chantaco": "Chantaco",
            "Chuquiribamba": "Chuquiribamba",
            "El_Cisne": "El_Cisne",
            "Gualel": "Gualel" }


def index(request):
    template='gastronomia/index.html'
    lista = Establecimiento.objects.all()
    return render(request,template, {
        "lista": lista
    })


def parroquias(request):
    context = {
        "parroquias": PARROQUIAS
    }
    return render(request, "gastronomia/parroquias.html", {
        "context": context
    })

class EstablecimientoViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows establecimientos to be viewed or edited.
    """
    #queryset = Establecimiento.objects.all().order_by('-precio_promedio')
    serializer_class = EstablecimientoSerializer
    def get_queryset(self):
        """
        Optionally restricts the returned purchases to a given user,
        by filtering against a `nombte`, `parroquia` or `precio` query parameter in the URL.
        """
        queryset = Establecimiento.objects.all().order_by('-precio_promedio')
        nombre = self.request.query_params.get('nombre')
        parroquia = self.request.query_params.get('parroquia')
        precio = self.request.query_params.get('precio')
        if nombre is not None:
            queryset = Establecimiento.objects.all()
            queryset = queryset.filter(nombre=nombre)
        if parroquia is not None:
            parroquia_values = parroquia.split(",")
            queryset = queryset.filter(parroquia__in=parroquia_values)
        if precio is not None:
            queryset = queryset.filter(precio_promedio__lte=precio)
        return queryset
    


class NombresViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows establecimientos nombres to be viewed or edited.
    """
    queryset = Establecimiento.objects.values('nombre')
    serializer_class = NombreSerializer
    