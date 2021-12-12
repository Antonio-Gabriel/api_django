from django.db import models
from .base import Base

class Curso(Base, models.Model):
    titulo = models.CharField(max_length=255)
    url = models.URLField(unique=True)

    class Meta:
        verbose_name = 'Curso'
        verbose_name_plural = 'Cursos'

        db_table = "curso"
    
    def __str__(self):
        return self.titulo