
from app.models import Livro
from app.exceptions import LivroNaoEncontradoException


# Acervo inicial da biblioteca armazenado em memória.
livros: list[Livro] = [
    Livro(
        id=1,
        titulo="Dom Casmurro",
        autor="Machado de Assis",
        ano_publicacao=1899,
        disponivel=True
    ),
    Livro(
        id=2,
        titulo="O Pequeno Príncipe",
        autor="Antoine de Saint-Exupéry",
        ano_publicacao=1943,
        disponivel=True
    ),
    Livro(
        id=3,
        titulo="1984",
        autor="George Orwell",
        ano_publicacao=1949,
        disponivel=False
    ),
    Livro(
        id=4,
        titulo="A Revolução dos Bichos",
        autor="George Orwell",
        ano_publicacao=1945,
        disponivel=True
    ),
    Livro(
        id=5,
        titulo="Capitães da Areia",
        autor="Jorge Amado",
        ano_publicacao=1937,
        disponivel=False
    )
]


# Retorna todos os livros cadastrados.
def listar_livros() -> list[Livro]:
    return livros


# Busca um livro pelo seu identificador.
def buscar_livro_por_id(livro_id: int) -> Livro:

    for livro in livros:
        if livro.id == livro_id:
            return livro

    # Lança uma exceção caso o livro não seja encontrado.
    raise LivroNaoEncontradoException(livro_id)
