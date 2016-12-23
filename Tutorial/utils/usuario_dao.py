from domain.usuario import Usuario
from utils.database import db_session


def add(us: Usuario) -> Exception:
    """Tenta adicionar um usuário. Se ok, retorna None, se não retorna o erro."""
    try:
        db_session.add(us)
        db_session.commit()
        return None

    except Exception as err:
        print("Erro tentando adicionar: {}".format(err))
        return err


def find(nome: str) -> Usuario:
    """Tenta encontrar um usuário pelo nome. Se ok, retorna-o, se não retorna None"""
    try:
        for usuario_db in db_session.query(Usuario).filter(Usuario.nome == nome):
            return usuario_db
    except Exception as err:
        print("Erro: {} procurando: {}".format(err, str))
        return None