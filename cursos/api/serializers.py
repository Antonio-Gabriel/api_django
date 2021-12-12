from cursos.entities import *

from rest_framework import serializers

class AvaliacaoSerializer(serializers.ModelSerializer):
    
    class Meta:
        extra_kwargs = {
            'email': {
                'write_only': True
            }
        }
        model = Avaliacao
        fields = "__all__"


class CursoSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Curso
        fields = "__all__"
