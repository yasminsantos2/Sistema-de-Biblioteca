from app.banco_de_dados.local import BancoDeDadosLocal
from app.modelos.livro import Livro

class LivroRepositorio:
    def __init__(self, banco_de_dados: BancoDeDadosLocal):
        self.db = banco_de_dados

    async def listar_livros(self) -> list[Livro]:
        with self.db.conectar() as conexao:
            cursor = conexao.cursor()
            cursor.execute("SELECT id, titulo, autor, categoria FROM livro")
            linhas = cursor.fetchall()
            return [
                Livro(id=linha[0], titulo=linha[1], autor=linha[2], categoria=linha[3])
                for linha in linhas
            ]

    async def obter_livro(self, livro_id: int) -> Livro | None:
        with self.db.conectar() as conexao:
            cursor = conexao.cursor()
            cursor.execute("SELECT id, titulo, autor, categoria FROM livro WHERE id = ?", (livro_id,))
            linha = cursor.fetchone()
            if linha:
                return Livro(id=linha[0], titulo=linha[1], autor=linha[2], categoria=linha[3])
            return None
