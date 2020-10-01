"""chacoferia URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from apps.publicaciones.views import Publicar, Articulo, NewPost, search, PublicarUser, ArticuloUser, searchUser
from apps.ayuda.views import ayuda, ayudaUser, about, aboutUser
from apps.tiendas.views import List_tienda, Registro_tienda, List_tiendaUser
from apps.inicio.views import Populares, PopularesUser
from apps.categorias.views import NewCategory, Category, category, filtrar, CategoryUser, categoryUser, filtrarUser
from .settings import base
from django.contrib.staticfiles.urls import static
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from apps.usuarios.views import NewUser, logout
from django.contrib.auth.views import LoginView
from carrito import views



urlpatterns = [
    path('admin/', admin.site.urls),
    path('', Populares.as_view(), name='inicio'),
    path('categorias/filtro', Category.as_view(),name='categorias'),
    path('categorias/', category,name='categoriasPrincipal'),
    path('categorias/filter', filtrar,name='filter'),
    path('publicaciones/publicaciones', Publicar.as_view(),name='publicaciones'),
    path('publicaciones/<int:pk>', Articulo.as_view(),name='detalleProducto'),
    path('publicaciones/search', search,name='search'),
    path('tienda/', List_tienda.as_view(),name='tienda'),
    path('usuario/new', NewUser.as_view(), name='newUsuario'),
    path('usuario/login',LoginView.as_view(template_name='usuarios/usuario.html'), name='login'),
    path('ayuda/', ayuda,name='ayuda'),
    path('ayuda/about', about,name='about'),

    path('cart/', include('carrito.urls')),
    path('orders/', include('ordenes.urls')),

    # ------------------------- URL USUARIOS -------------------------------------------
    path('usuario/', PopularesUser.as_view(), name='home'),
    path('categorias/new', NewCategory.as_view(),name='Newcategorias'),
    path('categorias/usuario/filtro', CategoryUser.as_view(),name='Categorias'),
    path('categorias/usuario/', categoryUser,name='CategoriasPrincipal'),
    path('categorias/usuario/filter', filtrarUser,name='Filter'),
    path('publicaciones/publicacionesusuario/', PublicarUser.as_view(),name='Publicaciones'),
    path('publicaciones/usuario/<int:pk>', ArticuloUser.as_view(),name='DetalleProducto'),
    path('publicaciones/new', NewPost.as_view(),name='new'),
    path('publicaciones/usuario/search', searchUser,name='Search'),
    path('tienda/usuario/', List_tiendaUser.as_view(),name='Tienda'),
    path('tienda/registro', Registro_tienda.as_view(), name='registro'),
    path('ayuda/usuario/', ayudaUser,name='Ayuda'),
    path('ayuda/usuario/about', aboutUser,name='About'),
    path('logout', logout, name='logout')

    
]
urlpatterns += staticfiles_urlpatterns()
urlpatterns += static(base.MEDIA_URL, document_root=base.MEDIA_ROOT)