from pydantic import BaseModel


class Livro(BaseModel):
    id: int 
    titulo: str
    autor: str
    categoria: str

class LivroCriarAtualizar(BaseModel):
    titulo: str
    autor: str
    categoria: str

