from django.urls import include, path

from . import views
#from django.views.generic import TemplateView
from gastronomia import views


urlpatterns = [
    path('', views.index, name='index'),
    path("parroquias", views.parroquias, name="parroquias"),
]