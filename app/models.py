
from pydantic import BaseModel, Field, ConfigDict


# Modelo que representa um livro da biblioteca.
class Livro(BaseModel):

    # Remove espaços extras e valida os campos de texto.
    model_config = ConfigDict(str_strip_whitespace=True)

    id: int = Field(gt=0, description="Identificador maior que zero")

    titulo: str = Field(min_length=1, description="Título do livro")

    autor: str = Field(min_length=1, description="Autor do livro")

    ano_publicacao: int = Field(gt=0, description="Ano de publicação maior que zero")

    disponivel: bool
