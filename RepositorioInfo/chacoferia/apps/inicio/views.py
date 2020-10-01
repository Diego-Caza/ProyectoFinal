from django.shortcuts import render
from apps.publicaciones.models import Producto
from  django.views.generic import ListView, DetailView, CreateView
# Create your views here.

class Populares(ListView):
	model = Producto
	template_name = 'inicio/inicio.html'
	queryset = Producto.objects.order_by('-id')[:4]

class PopularesUser(ListView):
	model = Producto
	template_name = 'inicio/usuario/inicio.html'
	queryset = Producto.objects.order_by('-id')[:4]

