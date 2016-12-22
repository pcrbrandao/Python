from domain.usuario import Usuario
from utils.database import db_session


def add(us: Usuario) -> Exception:

    try:
        db_session.add(us)
        db_session.commit()
        return None

    except Exception as err:
        print("Erro tentando adicionar: {}".format(err))
        return err