"""Provê a conexão com MySQL. Existem várias maneiras para fazer isso.
A Base está em domain pois as classes de dominio herdam dela."""

from sqlalchemy import create_engine
from sqlalchemy.orm import scoped_session, sessionmaker

# As classes devem ser importadas aqui para que o init_db possa criá-las.
import domain

engine = None
db_session = None

try:
    engine = create_engine('mysql+pymysql://root:root@localhost:8889/receitas')
    db_session = scoped_session(sessionmaker(autocommit=False,
                                             autoflush=False,
                                             bind=engine))
except Exception as err:
    print("Não pude conectar: {}".format(err))
    engine = None
    db_session = None

def init_db():
    """O IDE não oferece o metadata no autocomplete, mas está funcionando
    conforme a documentação do SQLAlchemy"""
    domain.Base.metadata.create_all(bind=engine)

