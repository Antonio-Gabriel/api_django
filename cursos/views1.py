from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

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
    
    def post(self, request) -> Response:
        serializer = CursoSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    
    def put(self, request, id: int) -> Response:        
        curso = Curso.objects.filter(id=id)
        print(curso)
        # updated_args = { **curso, **request.data }
        # serializer = CursoSerializer(data=updated_args)
        # serializer.is_valid(raise_exception=True)
        # serializer.update()
        return Response({"msg": ""}, status=status.HTTP_200_OK)


class AvaliacaoViewAPI(APIView):
    """
        API de avaliações
    """

    def get(self, request) -> Response:
        avaliacao = Avaliacao.objects.all()
        serializer = AvaliacaoSerializer(avaliacao, many=True)
        return Response(serializer.data)

    def post(self, request) -> Response:
        serializer = AvaliacaoSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)