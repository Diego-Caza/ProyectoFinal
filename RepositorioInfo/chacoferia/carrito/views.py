from django.shortcuts import render
from django.shortcuts import redirect
from apps.publicaciones.models import Producto
from django.contrib.auth.decorators import login_required
from .cart import Cart


@login_required(login_url='usuario/login')
def add_product(request, product_id):
    cart = Cart(request)
    product = Producto.objects.get(id=product_id)
    cart.add(product=product)
    return redirect("home")


@login_required(login_url='usuario/login')
def remove_product(request, product_id):
    cart = Cart(request)
    product = Producto.objects.get(id=product_id)
    cart.remove(product)
    return redirect("home")


@login_required(login_url='usuario/login')
def decrement_product(request, product_id):
    cart = Cart(request)
    product = Producto.objects.get(id=product_id)
    cart.decrement(product=product)
    return redirect("home")


@login_required(login_url='usuario/login')
def clear_cart(request):
    cart = Cart(request)
    cart.clear()
    return redirect("home")


