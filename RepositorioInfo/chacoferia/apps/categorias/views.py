from django.shortcuts import render
from .models import Categoria
from apps.publicaciones.models import Producto
from django.views.generic import ListView, DetailView, CreateView
from .forms import CategoriaForm
from django.urls import reverse
from django.http import HttpResponse
# Create your views here.

def category(request):
	categoriaPrincipal=Producto.objects.all
	return render(request, 'categorias/categorias.html', {'categoriaPrincipal':categoriaPrincipal})

def categoryUser(request):
	categoriaPrincipal=Producto.objects.all
	return render(request, 'categorias/usuario/categorias.html', {'categoriaPrincipal':categoriaPrincipal})

class NewCategory(CreateView):
	model = Categoria
	form_class = CategoriaForm
	template_name = 'categorias/usuario/categoriasNew.html'

	def get_success_url(self):
		return reverse('categorias')


class Category(ListView):
	model = Categoria
	template_name = 'categorias/filtro.html'

class CategoryUser(ListView):
	model = Categoria
	template_name = 'categorias/usuario/filtro.html'

def filtrar(request):
	q=int(request.GET["filter"].strip())
	categoria=Producto.objects.filter(categoria=q)
	return render(request, 'categorias/categoriasFilter.html', {'categoria':categoria})

def filtrarUser(request):
	q=int(request.GET["filter"].strip())
	categoria=Producto.objects.filter(categoria=q)
	return render(request, 'categorias/usuario/categoriasFilter.html', {'categoria':categoria})