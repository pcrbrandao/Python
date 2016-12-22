from sqlalchemy import create_engine
from sqlalchemy.orm import scoped_session, sessionmaker
from domain import Base
from domain.usuario import Usuario

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
    Base.metadata.create_all(bind=engine)

