from sqlalchemy import create_engine
from sqlalchemy.orm import Session
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import MetaData

metadata = MetaData()
Base = declarative_base(metadata=metadata)
engine = None
session = None

try:
    engine = create_engine('mysql+pymysql://root:root@localhost:8889/receitas')
    session = Session(engine)


except Exception as err:
    print("Não pude conectar: {}".format(err))
    engine = None
    session = None