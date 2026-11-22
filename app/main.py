
from fastapi import FastAPI, HTTPException, Path

from app.models import Livro
from app.repository import listar_livros, buscar_livro_por_id
from app.exceptions import LivroNaoEncontradoException


# Criação da aplicação FastAPI.
app = FastAPI(
    title="API da Biblioteca",
    description="API para consulta ao acervo de livros.",
    version="1.0.0"
)


# Rota para consultar todos os livros cadastrados.
@app.get("/livros", response_model=list[Livro])
def consultar_livros() -> list[Livro]:

    return listar_livros()


# Rota para consultar um livro pelo identificador.
@app.get("/livros/{livro_id}", response_model=Livro)
def consultar_livro(
    livro_id: int = Path(
        gt=0,
        description="ID do livro deve ser maior que zero"
    )
) -> Livro:

    try:
        return buscar_livro_por_id(livro_id)

    except LivroNaoEncontradoException as erro:

        # Converte a exceção personalizada em resposta HTTP 404.
        raise HTTPException(
            status_code=404,
            detail=str(erro)
        )
