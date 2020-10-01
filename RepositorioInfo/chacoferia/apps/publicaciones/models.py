from django.db import models
from apps.categorias.models import Categoria

# Create your models here.

class Producto(models.Model):
    nombre = models.CharField(max_length=100)
    slug = models.SlugField(default='nombre')
    categoria = models.ForeignKey(Categoria, on_delete=models.CASCADE)
    imagen = models.ImageField(upload_to='photos', blank=True)
    texto_corto = models.TextField(max_length=200, verbose_name='Extracto')
    detalle = models.TextField(max_length=1000, verbose_name='Información del producto')
    precio = models.FloatField()
    avalible = models.BooleanField(default=True)

    def __str__(self):
        return self.nombre

    class Meta:
        db_table = 'productos'
        verbose_name = 'Producto'
        verbose_name_plural = 'Productos'
        ordering = ['id']


    


