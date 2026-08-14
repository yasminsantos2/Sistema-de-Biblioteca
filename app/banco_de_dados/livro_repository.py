from app.banco_de_dados.local import BancoDeDadosLocal
from app.modelos.livro import Livro, LivroCriarAtualizar

# Faz a ponte entre o banco (linhas SQL) e os objetos Livro.
class LivroRepositorio:

    # Recebe o banco de fora (injeção de dependência).
    def __init__(self, banco_de_dados: BancoDeDadosLocal):
        self.bd = banco_de_dados

    # Retorna todos os livros como lista de objetos Livro.
    async def listar_livros(self) -> list[Livro]:
        with self.bd.conectar() as conexao:           # abre e fecha conexão sozinho
            cursor = conexao.cursor()                 # ponteiro para executar SQL
            cursor.execute("SELECT id, titulo, autor, categoria FROM livro")
            linhas = cursor.fetchall()                # traz todas as linhas (tuplas)

            # Converte cada tupla em um objeto Livro.
            livros = [
                Livro(
                    id=linha[0],
                    titulo=linha[1],
                    autor=linha[2],
                    categoria=linha[3]
                )
                for linha in linhas
            ]
            return livros

    async def obter_livro(self, livro_id: int) -> Livro | None:
        with self.bd.conectar() as conexao:
            cursor = conexao.cursor()
            cursor.execute(
                "SELECT id, titulo, autor, categoria FROM livro WHERE id = ?",
                (livro_id,)
            )
            linha = cursor.fetchone()  # traz uma única linha (tupla)

            if linha is None:
                return None

            return Livro(
                id=linha[0],
                titulo=linha[1],
                autor=linha[2],
                categoria=linha[3]
            )

    async def criar_livro(self, livro: LivroCriarAtualizar) -> Livro:
        with self.bd.conectar() as conexao:
            cursor = conexao.cursor()
            cursor.execute(
                "INSERT INTO livro (titulo, autor, categoria) VALUES (?, ?, ?)",
                (livro.titulo, livro.autor, livro.categoria),
            )
            livro_id = cursor.lastrowid
            return Livro(id=livro_id, titulo=livro.titulo, autor=livro.autor, categoria=livro.categoria)

    async def atualizar_livro(self, livro_id: int, livro: LivroCriarAtualizar) -> Livro | None:
        with self.bd.conectar() as conexao:
            cursor = conexao.cursor()
            cursor.execute(
                "UPDATE livro SET titulo = ?, autor = ?, categoria = ? WHERE id = ?",
                (livro.titulo, livro.autor, livro.categoria, livro_id)
            )
            if cursor.rowcount == 0:
                return None
            return Livro(id=livro_id, titulo=livro.titulo, autor=livro.autor, categoria=livro.categoria)

    async def deletar_livro(self, livro_id: int) -> bool:
        with self.bd.conectar() as conexao:
            cursor = conexao.cursor()
            cursor.execute(
                "DELETE FROM livro WHERE id = ?", (livro_id,)
            )
            return cursor.rowcount > 0
