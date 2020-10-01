from django.db import models

# Create your models here.

class Categoria(models.Model):
    nombre = models.CharField(max_length=300)
    destacado = models.BooleanField(default=False)

    def __str__(self):
        return self.nombre

    class Meta:
        db_table = 'categoria'
        verbose_name = 'Categoría'
        verbose_name_plural = 'Categorías'
        ordering = ['id']

    

