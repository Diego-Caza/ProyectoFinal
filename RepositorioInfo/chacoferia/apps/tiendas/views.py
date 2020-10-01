from django.shortcuts import render
from .models import Tienda
from django.views.generic import ListView, DetailView, CreateView
from .forms import TiendaForm
from django.urls import reverse

# Create your views here.

class Registro_tienda(CreateView):
    model = Tienda
    form_class = TiendaForm
    template_name = 'tiendas/usuario/registrar.html'

    def get_success_url(self):
        return reverse('registro')


class List_tienda(ListView):
    model = Tienda
    template_name = 'tiendas/tienda.html'

class List_tiendaUser(ListView):
    model = Tienda
    template_name = 'tiendas/usuario/tienda.html'