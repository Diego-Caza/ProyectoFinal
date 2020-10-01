from django.db import models

# Create your models here.

class Tienda(models.Model):
    nombre_tienda = models.CharField(max_length = 100)
    descripcion = models.TextField()
    imagen = models.ImageField(upload_to='photos', blank=True)
    ubicacion = models.CharField(max_length = 100)
    ##nombre = models.ForeignKey(Perfil, on_delete = models.CASCADE)



    def __str__(self):
        return self.nombre

    class Meta:
        db_table = 'tienda'
        verbose_name = 'Tiendas'
        verbose_name_plural = 'Tiendas'
        ordering = ['id']

