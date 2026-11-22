API DA BIBLIOTECA

1.  DESCRICAO DO PROJETO

Este projeto consiste em uma API desenvolvida com Python e FastAPI para
consultar o acervo de uma biblioteca.

A API permite listar todos os livros cadastrados e consultar um livro
específico pelo seu identificador (ID). Os dados são armazenados em
memória, sem utilização de banco de dados.

2.  TECNOLOGIAS UTILIZADAS

-   Python
-   FastAPI
-   Pydantic
-   Uvicorn

3.  ESTRUTURA DO PROJETO

api_biblioteca/ | |– app/ | |– main.py | |– models.py | |– repository.py
| |– exceptions.py | |– venv/ | |– requirements.txt | |– README.txt

4.  DESCRICAO DOS ARQUIVOS

main.py: Arquivo principal da aplicação. Inicializa o FastAPI, define as
rotas e converte a exceção de livro não encontrado em uma resposta HTTP
404.

models.py: Define o modelo Livro e as validações dos campos: ID, título,
autor, ano de publicação e disponibilidade.

repository.py: Mantém a lista de livros em memória e implementa as
funções para listar todos os livros e buscar um livro pelo ID.

exceptions.py: Define a exceção personalizada
LivroNaoEncontradoException, utilizada quando o livro solicitado não
existe no acervo.

requirements.txt: Lista as dependências necessárias para executar o
projeto.

5.  INSTALACAO

Pré-requisito: Ter o Python instalado no computador.

Abra o terminal na pasta principal do projeto e execute os comandos:

Criar o ambiente virtual:

python -m venv venv

Ativar o ambiente virtual no Windows PowerShell:

venv.ps1

Instalar as dependências:

pip install -r requirements.txt

Caso as dependências ainda não estejam listadas no arquivo
requirements.txt, ele deve conter:

fastapi uvicorn

6.  COMO EXECUTAR A API

Com o ambiente virtual ativado, execute na pasta principal do projeto:

uvicorn app.main:app –reload

Quando o servidor iniciar corretamente, a API estará disponível em:

http://127.0.0.1:8000

Para acessar a documentação interativa do FastAPI (Swagger), abra:

http://127.0.0.1:8000/docs

7.  ROTAS DISPONIVEIS

GET /livros

Retorna a lista de todos os livros cadastrados no acervo.

Exemplo de acesso:

http://127.0.0.1:8000/livros

GET /livros/{livro_id}

Retorna os dados do livro correspondente ao ID informado.

Exemplo de acesso:

http://127.0.0.1:8000/livros/1

8.  RESPOSTAS E VALIDACOES

Na consulta de um livro pelo ID, a API pode retornar:

200 OK: O livro foi encontrado e seus dados são retornados em formato
JSON.

404 Not Found: O ID é válido, mas não existe livro cadastrado com esse
identificador.

422 Unprocessable Entity: O identificador informado é inválido, como
zero, número negativo ou texto que não representa um número inteiro.

Na listagem, a API retorna 200 OK e uma lista JSON. Se não houver livros
cadastrados, a lista retornada será vazia.

9.  ACERVO INICIAL

O repositório contém cinco livros cadastrados em memória:

-   ID 1: Dom Casmurro - Machado de Assis
-   ID 2: O Pequeno Príncipe - Antoine de Saint-Exupéry
-   ID 3: 1984 - George Orwell
-   ID 4: A Revolução dos Bichos - George Orwell
-   ID 5: Capitães da Areia - Jorge Amado

Os dados ficam armazenados em memória e são reiniciados quando a
aplicação é encerrada ou reiniciada.

10. TESTES REALIZADOS

Foram realizados testes das rotas e das validações:

-   GET /livros: 200 OK.
-   GET /livros/1: 200 OK.
-   GET /livros/10: 404 Not Found.
-   GET /livros/0: 422 Unprocessable Entity.
-   GET /livros/-1: 422 Unprocessable Entity.
-   GET /livros/abc: 422 Unprocessable Entity.

11. OBSERVACOES

A aplicação utiliza separação de responsabilidades: o modelo define e
valida os dados, o repositório controla o acesso à coleção de livros, a
classe de exceção representa o livro não encontrado e o arquivo
principal disponibiliza as rotas HTTP.

Para encerrar o servidor, pressione CTRL + C no terminal.
