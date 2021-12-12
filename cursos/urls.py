from django.urls import path

from .views import CursoAPIView, AvaliacaoAPIView, AvaliacoesAPIView, CursosAPIView

urlpatterns = [
    path('cursos/', CursosAPIView().as_view(), name="cursos"),
    path('cursos/<int:pk>/', CursoAPIView().as_view(), name="curso"),

    path(
        'cursos/<int:curso_pk>/avaliacoes', 
        AvaliacoesAPIView().as_view(), name="curso_avaliacoes"),
    
    path(
        'cursos/<int:curso_pk>/avaliacoes/<int:avaliacao_pk>', 
        AvaliacaoAPIView().as_view(), name="curso_avaliacoes"),

    path('avaliacoes/', AvaliacoesAPIView().as_view(), name="avaliacoes"),
    path('avaliacoes/<int:avaliacao_pk>/', AvaliacaoAPIView().as_view(), name="avaliacao"),
]