from django.shortcuts import render
from apps.publicaciones.models import Producto
from django.views.generic import ListView, DetailView, CreateView
from .forms import ProductoForm
from django.urls import reverse
from django.http import HttpResponse
# Create your views here.

class Publicar(ListView):
	model = Producto
	template_name = 'publicaciones/public.html'

class PublicarUser(ListView):
	model = Producto
	template_name = 'publicaciones/usuario/public.html'

class Articulo(DetailView):
	model = Producto
	template_name = 'publicaciones/detalleProducto.html'

class ArticuloUser(DetailView):
	model = Producto
	template_name = 'publicaciones/usuario/detalleProducto.html'

class NewPost(CreateView):
	model = Producto
	form_class = ProductoForm
	template_name = 'publicaciones/usuario/publicaciones.html'

	def get_success_url(self):
		return reverse('usuario/publicaciones')

def search(request):
	q=request.GET["buscar"].strip()
	producto=Producto.objects.filter(nombre__icontains=q)
	return render(request, 'buscar/buscar.html', {'producto':producto})

def searchUser(request):
	q=request.GET["buscar"].strip()
	producto=Producto.objects.filter(nombre__icontains=q)
	return render(request, 'buscar/usuario/buscar.html', {'producto':producto})