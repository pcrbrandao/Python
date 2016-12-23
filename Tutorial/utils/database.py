"""Provê a conexão com MySQL. Existem várias maneiras para fazer isso.
A Base está em domain pois as classes de dominio herdam dela."""

from sqlalchemy import create_engine
from sqlalchemy.orm import scoped_session, sessionmaker, Session
from sqlalchemy.engine import Engine

# As classes devem ser importadas aqui para que o init_db possa criá-las.
import domain


def get_engine() -> Engine:
    try:
        return create_engine('mysql+pymysql://root:root@localhost:8889/receitas')

    except Exception as err:
        print("Não pude conectar: {}".format(err))
        return err

def get_db_session(engine: Engine) -> Session:
    return scoped_session(sessionmaker(autocommit=False,
                                       autoflush=False,
                                       bind=engine))

engine = get_engine()
db_session = get_db_session(engine)

def init_db():
    """O IDE não oferece o metadata no autocomplete, mas está funcionando
    conforme a documentação do SQLAlchemy"""
    domain.Base.metadata.create_all(bind=engine)

