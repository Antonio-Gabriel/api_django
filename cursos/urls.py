from django.urls import path

from .views import CursoViewAPI, AvaliacaoViewAPI

urlpatterns = [
    path('cursos/', CursoViewAPI().as_view(), name="cursos"),
    path('avaliacoes/', AvaliacaoViewAPI().as_view(), name="avaliacoes"),
]