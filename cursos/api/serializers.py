from cursos.entities import *

from rest_framework import serializers
from django.db.models import Count

class AvaliacaoSerializer(serializers.ModelSerializer):
    
    class Meta:
        extra_kwargs = {
            'email': {
                'write_only': True
            }
        }
        model = Avaliacao
        fields = "__all__"
    
    def validate_avaliacao(self, valor):
        if valor in range(1, 6):
            return valor
            
        return serializers.ValidationError(
            'A Avaliação precisa ser um inteiro entre 1 a 5'
            )


class CursoSerializer(serializers.ModelSerializer):
    # Nested Relationship
    # avaliacoes = AvaliacaoSerializer(many=True, read_only=True)

    # HyperLinked Related Field
    avaliacoes = serializers.HyperlinkedRelatedField(
            many=True, 
            read_only=True, 
            view_name="avaliacao-detail"
            )            

    # total_course = serializers.SerializerMethodField()

    class Meta:
        model = Curso
        # fields = "__all__"
        fields =  (
            'id',
            'titulo',
            'url',
            'ativo',
            'criacao',
            'atualizacao',
            'avaliacoes',               
        )
    

    def get_total_course(self, obj):
        #return obj.titulo(Count('id')).get('id__count')
        pass