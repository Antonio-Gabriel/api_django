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