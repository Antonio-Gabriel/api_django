from django.db import models
from .base import Base

from .curso import Curso

class Avaliacao(Base, models.Model):
    curso = models.ForeignKey(Curso, related_name='avaliacoes', on_delete=models.CASCADE)
    nome = models.CharField(max_length=255)
    email = models.EmailField()
    comentario = models.TextField(blank=True, default='')
    avaliacao = models.DecimalField(max_digits=2, decimal_places=1) # Para poder usar 4.1, 1.8

    class Meta:
        verbose_name = "Avaliação"
        verbose_name_plural = "Avaliações"
        
        ordering = ['id']

        # Restringir para o usuários avaliar unicamente um curso
        unique_together = ['email', 'curso'] 
        db_table = "avaliacao"

    def __str__(self):
        return f'{self.nome} avaliou o curso {self.curso} com nota {self.avaliacao}'