from django.db import models

# Create your models here.

#Noticia
class Noticia(models.Model):
    titulo = models.CharField(max_length=200)
    contenido = models.TextField()
    fecha_publicacion = models.DateField()

    def __str__(self):
        return self.titulo