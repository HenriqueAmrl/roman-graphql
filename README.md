# Tecnologias utilizadas
- Linguagem de programação: Python 3.10
- Gerenciador de pacotes: Poetry | Pip
- Framework HTTP: Flask
- Framework GraphQL: Graphene
- Framework de testes: Pytest
- Servidor WSGI: Gunicorn

# Estrutura do projeto

> Estrutura de arquivos e convenções de nomes utilizados

### Estrutura básica de pastas

A pasta `app` contém toda a  estrutura do sistema.

    app
    ├── app.py                  # App Flask
    ├── domain
    ├── graphql
    └── __init__.py


### /domain

Na pasta `domain` estão contidas as regras de negócio e testes de subdomínios. Para seguir um padrão de arquitetura, códigos desses módulos não podem tratar de dados HTML ou GraphQL.

    domain
    └── dominio-do-sistema
        ├── actions.py          # Regras de negócio que podem ser reutilizadas, seguindo o padrão facade
        ├── entity.py           # Classes que representam os objetos utilizados pelo módulo
        ├── __init__.py         # Importa dos arquivos anteriores, para permitir que sejam usados fora do módulo
        └── tests
            ├── actions_test.py
            ├── conftest.py
            ├── entity_test.py

### /graphql

Na pasta `graphql` estão contidas as queries e mutations que interligam a API GraphQL com a camada de domínio.

    graphql
    ├── __init__.py         # View GraphQL (Usada pelo Flask)
    ├── dominio-graphql
    │   ├── __init__.py     # Agrupa as queries e mutations do pacote
    │   ├── mutations.py
    │   └── queries.py
    └── schema.py           # Todos os schemas de domínios GraphQL são unificados aqui

> **Padrões de projeto**: [Service Layer](https://www.cosmicpython.com/book/chapter_04_service_layer.html), [Clean Architeture](https://medium.com/luizalabs/descomplicando-a-clean-architecture-cf4dfc4a1ac6), [App factory](https://flask.palletsprojects.com/en/2.1.x/patterns/appfactories/)

# Testes automatizados

Testes automatizados estão localizados na pasta `tests` de cada domínio do sistema.

Para realizar os testes, instale as dependências de teste: `poetry install` e, em seguida, execute os testes: `pytest`

# Executando o projeto
## Com Docker
> Recomendado em produção

O projeto utiliza a tecnologia de container Docker.
Para iniciar o servidor:

- Crie a imagem: `docker build -t teste_henriqueamaral:latest .`
- Suba o container a partir da imagem criada: `docker run -p 8080:8080 teste_henriqueamaral:latest`

## Com Poetry
Também é possível usar o gerenciador de dependências Poetry. Através dele é possível criar um ambiente virtual e instalar as dependências automaticamente.

- `poetry install`
- `poetry shell`
- Inicie o servidor:
  - Desenvolvimento: `python wsgi.py`
  - Produção: `gunicorn wsgi:app -b 0.0.0.0:8080`

## Modo tradicional
O projeto pode ser executado diretamente no sistema, através de um ambiente virtual.

- Crie o virtualenv: `python -m venv .venv` ( no linux, `python3 -m venv .venv` )
- Ative o ambiente criado: `.venv/Scripts/Activate` ( no linux `source .venv/bin/activate` )
- instale as dependências: `pip install -r requirements.txt`
- Inicie o servidor:
  - Desenvolvimento: `python wsgi.py`
  - Produção: `gunicorn wsgi:app -b 0.0.0.0:8080`
