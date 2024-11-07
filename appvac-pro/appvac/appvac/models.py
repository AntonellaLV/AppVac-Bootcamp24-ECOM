from django.db import models

# Create your models here.

class Proyecto(models.Model):
    titulo = models.CharField(max_length=200)
    descripcion = models.TextField()
    imagen = models.ImageField(upload_to='imagenes/')
    fecha = models.DateField()
    enlace = models.URLField()

    def __str__(self):
        return self.titulo
