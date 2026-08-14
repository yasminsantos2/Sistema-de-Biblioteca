from typing import Annotated
from fastapi import APIRouter,  Depends, HTTPException

from app.dependencias import obter_livro_repositorio
from app.banco_de_dados.livro_repository import LivroRepositorio
from app.modelos.livro import Livro


router = APIRouter(
    prefix="/livros"
)

LIVRO_LIST = [
        Livro(id=1, titulo="O Senhor dos Anéis", autor="J.R.R. Tolkien", categoria="Fantasia"),
        Livro(id=2, titulo="1984", autor="George Orwell", categoria="Distopia"),
    ]


# ROTA PARA LISTAR TODOS OS LIVROS
@router.get("/", response_model=list[Livro])
async def listar_livros(livro_repositorio: Annotated["LivroRepositorio", Depends(obter_livro_repositorio)]):
    return await livro_repositorio.listar_livros()


# ROTA PARA OBTER UM LIVRO PELO ID
@router.get("/{livro_id}", response_model=Livro | None)
async def obter_livro(livro_id: int, livro_repositorio: Annotated["LivroRepositorio", Depends(obter_livro_repositorio)]):

    livro = await livro_repositorio.obter_livro(livro_id)
    if not livro:
        raise HTTPException(status_code=404, detail="Livro não encontrado")
    return livro



# ROTA PARA CRIAR UM NOVO LIVRO
@router.post("/", response_model=Livro, status_code=201)
async def criar_livro(
    livro: Livro,
    livro_repositorio: Annotated["LivroRepositorio", Depends(obter_livro_repositorio)]
):
    return await livro_repositorio.criar_livro(livro)


# ROTA PARA ATUALIZAR UM LIVRO EXISTENTE
@router.put("/{livro_id}", response_model=Livro)
async def atualizar_livro(
    livro_id: int,
    livro: Livro,
    livro_repositorio: Annotated["LivroRepositorio", Depends(obter_livro_repositorio)]
):
    livro_atualizado = await livro_repositorio.atualizar_livro(livro_id, livro)
    if not livro_atualizado:
        raise HTTPException(status_code=404, detail="Livro não encontrado")
    return livro_atualizado



