from controllers import session
from domain.usuario import Usuario


def add(us: Usuario) -> Exception:

    try:
        session.add(us)
        session.commit()
        return None

    except Exception as err:
        print("Erro tentando adicionar: {}".format(err))
        return err