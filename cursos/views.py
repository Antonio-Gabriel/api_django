from rest_framework.views import APIView
from rest_framework.response import Response

from cursos.entities import *
from cursos.api import *


class CursoViewAPI(APIView):
    """
        API de cursos
    """

    def get(self, request) -> Response:        
        cursos = Curso.objects.all()
        serializer = CursoSerializer(cursos, many=True)
        return Response(serializer.data)


class AvaliacaoViewAPI(APIView):
    """
        API de avaliações
    """

    def get(self, request) -> Response:
        avaliacao = Avaliacao.objects.all()
        serializer = AvaliacaoSerializer(avaliacao, many=True)
        return Response(serializer.data)