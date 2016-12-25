from domain.usuario import Usuario
from utils.database import db_session
from sqlalchemy.orm.query import Query
from utils.singleton import Singleton
from utils.paginas import Paginas


class UsuarioDAO(Singleton):
    """Fornece funções para acesso ao banco de dados"""

    def __init__(self, usuarios_por_pagina:int = 10, total_de_usuarios:int = 0):
        Singleton.__init__(self)
        self.usuarios_por_pagina = usuarios_por_pagina
        self.total_de_usuarios = 0
        self.paginas = Paginas()

    def add(self, usuario: Usuario) -> Exception:
        """Tenta adicionar um usuário. Se ok, retorna None, se não retorna o erro."""
        try:
            db_session.add(usuario)
            db_session.commit()
            return None

        except Exception as err:
            print("Erro tentando adicionar: {}".format(err))
            return err

    def find(self, nome: str) -> Usuario:
        """Tenta encontrar um usuário pelo nome. Se ok, retorna-o, se não retorna None"""
        try:
            query = db_session.query(Usuario).filter(Usuario.nome == nome)
            usuario_db = query.one_or_none()
            return usuario_db
        except Exception as err:
            print("Erro: {} procurando: {}".format(err, str))
            return None


    def delete(self, usuario: Usuario) -> Exception:
        """Tenta deletar um usuário. Se ok, retorna None, ou erro caso contrário"""
        try:
            db_session.delete(usuario)
            db_session.commit()
            return None
        except Exception as err:
            print("Erro: {}. {} não pode ser deletado".format(err, usuario))
            return err

    def list(self, pag_inic=0, pag_fim=0) -> Query:
        """Tenta retornar a lista dos usuários já com o limite por página"""

        if pag_fim < pag_inic or pag_inic < 0:
            print("páginas {}, {} inválidas".format(pag_inic, pag_fim))
            return None

        try:
            query = db_session.query(Usuario).order_by(Usuario.id).all()
            self.total_de_usuarios = len(query)

            if self.total_de_usuarios == 0:
                return None

            if pag_fim > len(query):
                pag_fim = len(query) - 1

            reg_ini = self.paginas.primeiro_registro_da_pagina(pag_inic, self.usuarios_por_pagina)
            reg_fim = self.paginas.ultimo_registro_da_pagina(pag_fim, self.usuarios_por_pagina,self.total_de_usuarios)

            return query[reg_ini:reg_fim]

        except Exception as err:
            print("não pude obter a query: {}".format(err))
            return None

    def delete_all(self):
        """Deleta todos os usuários no db!"""
        query = db_session.query(Usuario).all()

        for usuario in query:
            db_session.delete(usuario)
        db_session.commit()