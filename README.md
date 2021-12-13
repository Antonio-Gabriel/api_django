# Plataforma de cursos

Uma plataforma minimalista desenvolvida com django, aplicando alguns recursos descobertos que de certa forma dariam uma melhor organizada no código.

A aplicação basicamente registra cursos e o usuário atribui avaliação para os cursos presentes na plataforma de acordo aos seus gostos.

```bash    
python manage.py makemigrations
python manage.py sqlmigrate
python manage.py migrate    
```

Antes crie um usuário para assim poderes navegar pela aplicação.

> user: admin

> password: antoniocampos20

Depois já podes rodar a aplicação, o comando sqlmigrate é basicamente para conseguir obter uma preview do código sql gerado para a criação das tabelas na base de dados.

```bash    
python manage.py runserver
```

## Gerando paginação a partir de ViewSet

De uma forma dinâmica foi fácil e símples gerar a paginação a partir das viewsets

```python
class CursoViewSet(viewsets.ModelViewSet):
    queryset = Curso.objects.all()
    serializer_class = CursoSerializer

    @action(detail=True, methods=['get'])
    def avaliacoes(self, request, pk=None):
        # Definir paginação interna
        self.pagination_class.page_size = 1
        avaliacoes = Avaliacao.objects.filter(curso_id=pk)
        page = self.paginate_queryset(avaliacoes)

        if page is not None:
            serializer = AvaliacaoSerializer(page, many=True)
            return self.get_paginated_response(serializer.data)

        # curso = self.get_object()
        # serializer = AvaliacaoSerializer(curso.avaliacoes.all(), many=True)
        #         
        serializer = AvaliacaoSerializer(avaliacoes, many=True)
        return Response(serializer.data)
```