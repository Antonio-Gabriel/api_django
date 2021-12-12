from rest_framework import generics
from rest_framework.generics import get_object_or_404

from rest_framework import viewsets
from rest_framework.decorators import action
from rest_framework.response import Response

from cursos.entities import *
from cursos.api import *

# API Version 1

class CursosAPIView(generics.ListCreateAPIView):
    queryset=Curso.objects.all()
    serializer_class = CursoSerializer

class CursoAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset=Curso.objects.all()
    serializer_class = CursoSerializer

class AvaliacoesAPIView(generics.ListCreateAPIView):
    queryset=Avaliacao.objects.all()
    serializer_class = AvaliacaoSerializer

    def get_queryset(self):
        if self.kwargs.get("curso_id"):
            return self.queryset.filter(curso_id=self.kwargs.get("curso_id"))
        return self.queryset.all()

class AvaliacaoAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset=Avaliacao.objects.all()
    serializer_class = AvaliacaoSerializer    

    def get_object(self):
        if self.kwargs.get("curso_pk"):
            return get_object_or_404(
                    self.get_queryset(), 
                    curso_id=self.kwargs.get("curso_pk"), 
                    pk=self.kwargs.get("avaliacao_pk")
                    )

        return get_object_or_404(
                self.get_queryset(),                 
                pk=self.kwargs.get("avaliacao_pk")
                )


# API Version 2

class CursoViewSet(viewsets.ModelViewSet):
    queryset = Curso.objects.all()
    serializer_class = CursoSerializer

class AvaliacaoViewSet(viewsets.ModelViewSet):
    queryset = Avaliacao.objects.all()
    serializer_class = AvaliacaoSerializer