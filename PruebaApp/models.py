from __future__ import unicode_literals

from django.db import models

# Create your models here.

class Post(models.Model):
    
    autor = models.ForeignKey('auth.User', on_delete=models.PROTECT)
    titulo = models.CharField(max_length=200)
    texto = models.TextField()
    fecha_creacion = models.DateTimeField(auto_now_add=True)