from domain.usuario import Usuario
from utils.database import db_session
from sqlalchemy.orm.query import Query

_usuarios_por_pagina = 10
_total_de_usuarios = 0


def usuarios_por_pagina() -> int: return _usuarios_por_pagina
def total_de_registros() -> int: return _total_de_usuarios

def total_de_paginas(total_de_registros:int, registros_por_pagina:int) -> int:
    """total das páginas. 10 siginifica que a primeira página é 0 e a última 9."""
    if total_de_registros <= 0:
        return 0

    if total_de_registros % registros_por_pagina == 0:
        return (total_de_registros // registros_por_pagina)

    return (total_de_registros // registros_por_pagina) + 1

def primeiro_registro_da_pagina(pagina:int, registros_por_pagina:int) -> int:
    """a primeira página é 0 (zero)"""
    return pagina * registros_por_pagina

def ultimo_registro_da_pagina(pagina:int, registros_por_pagina:int) -> int:
    """se a página é 2 e o registros_por_pagina é 10, então retorna 19"""
    return primeiro_registro_da_pagina(pagina,registros_por_pagina) + registros_por_pagina - 1

def add(usuario: Usuario) -> Exception:
    """Tenta adicionar um usuário. Se ok, retorna None, se não retorna o erro."""
    try:
        db_session.add(usuario)
        db_session.commit()
        return None

    except Exception as err:
        print("Erro tentando adicionar: {}".format(err))
        return err


def find(nome: str) -> Usuario:
    """Tenta encontrar um usuário pelo nome. Se ok, retorna-o, se não retorna None"""
    try:
        query = db_session.query(Usuario).filter(Usuario.nome == nome)
        usuario_db = query.one_or_none()
        return usuario_db
    except Exception as err:
        print("Erro: {} procurando: {}".format(err, str))
        return None


def delete(usuario: Usuario) -> Exception:
    """Tenta deletar um usuário. Se ok, retorna None, ou erro caso contrário"""
    try:
        db_session.delete(usuario)
        db_session.commit()
        return None
    except Exception as err:
        print("Erro: {}. {} não pode ser deletado".format(err, usuario))
        return err

def list(pag_inic:int, pag_fim:int) -> Query:
    """Tenta retornar a lista dos usuários já com o limite por página"""

    if pag_fim < pag_inic or pag_inic < 0:
        print("páginas {}, {} inválidas".format(pag_inic, pag_fim))
        return None

    try:
        query = db_session.query(Usuario).order_by(Usuario.id)
        _total_de_usuarios = len(query)

        if _total_de_usuarios == 0:
            return None

        if pag_fim > len(query):
            pag_fim = len(query) - 1

        return query[pag_inic:pag_fim]

    except Exception as err:
        print("não pude obter a query: {}".format(err))
        return None
