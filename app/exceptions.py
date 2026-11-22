
# Exceção personalizada para representar livros não encontrados.
class LivroNaoEncontradoException(Exception):

    def __init__(self, livro_id: int):
        self.livro_id = livro_id

        super().__init__(
            f"Livro com ID {livro_id} não encontrado."
        )
