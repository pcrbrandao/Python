from sqlalchemy import Column, Integer, String, Sequence
from controllers import Base


class Usuario(Base):
    'Representa um usuário do sistema para o SQLAlchemy'

    __tablename__ = 'usuarios'

    id = Column(Integer, Sequence('usuarios_id_seq'), primary_key=True)
    nome = Column(String(50))
    email = Column(String(50))
    senha = Column(String(12))

    def __repr__(self):
        return "<Usuario(nome='%s', email='%s', senha='%s')>" % (
            self.nome, self.email, self.senha)