from fastapi import APIRouter
from app.modelos.livros import Livro

router = APIRouter(
    prefix="/livros"
)

LIVRO_LIST = [
        Livro(id=1, titulo="O Senhor dos Anéis", autor="J.R.R. Tolkien", categoria="Fantasia"),
        Livro(id=2, titulo="1984", autor="George Orwell", categoria="Distopia"),
    ]



@router.get("/", response_model=list[Livro])
async def listar_livros():


    return LIVRO_LIST


@router.get("/{livro_id}", response_model=Livro | None)
async def obter_livro(livro_id: int):
    for livro in LIVRO_LIST:
        if livro.id == livro_id:
            return livro
    return None
