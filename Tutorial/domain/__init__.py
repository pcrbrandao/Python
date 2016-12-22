from controllers import metadata, engine
from domain.usuario import Usuario

metadata.create_all(engine,tables=[Usuario])

