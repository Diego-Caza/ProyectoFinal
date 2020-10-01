from django.db import models
from apps.tiendas.models import Tienda
# Create your models here.

class Perfil(models.Model):
    nombre = models.CharField(max_length=30)
    apellido = models.CharField(max_length=30)
    dni = models.CharField(max_length=30)
    tel = models.CharField(max_length=30)
    id_tienda = models.ForeignKey(Tienda, on_delete=models.CASCADE)
    

    def __str__(self):
        text = "{0} , {1}"
        return text.format(self.nombre,self.apellido)
    
    class Meta:
        db_table = 'perfil'
        verbose_name = 'Perfil'
        verbose_name_plural = 'Perfiles'
        ordering = ['id']