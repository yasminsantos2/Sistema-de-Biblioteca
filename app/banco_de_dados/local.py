
import sqlite3
from contextlib import contextmanager



class BancoDeDadosLocal():

    def __init__(self, nome_arquivo='livro.db'):
        self.nome_arquivo = nome_arquivo
        self.inicializar_banco()


    @contextmanager
    def conectar(self):

        conexao = sqlite3.connect(self.nome_arquivo)

        try:
            yield conexao
            conexao.commit()

        except Exception as e:
            conexao.rollback()

            raise e

        finally:

            conexao.close()


    def inicializar_banco(self):

        with self.conectar() as conexao:

            cursor = conexao.cursor()

            cursor.execute('''
                CREATE TABLE IF NOT EXISTS livro (

                    -- Identificador único do livro.
                    -- É gerado automaticamente pelo SQLite.
                    id INTEGER PRIMARY KEY AUTOINCREMENT,

                    -- Título obrigatório.
                    titulo TEXT NOT NULL,

                    -- Autor obrigatório.
                    autor TEXT NOT NULL,

                    -- Categoria obrigatória.
                    categoria TEXT NOT NULL

                )
            ''')