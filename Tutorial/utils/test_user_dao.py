import unittest

from domain.usuario import Usuario
from utils.usuario_dao import UsuarioDAO


class TestUserDAO(unittest.TestCase):
    """Os testes ainda não consideram todas as situações. Em desenvolvimento!"""

    dao = UsuarioDAO()

    def test_add_deve_retornar_none(self):
        """Acrescenta um usuário. Se não retornar erro está ok."""

        usuario = Usuario(nome='Pedro', email='email', senha='1234')
        result = self.dao.add(usuario)

        # o usuário deve ser encontrado no db
        usuario_db = self.dao.find("Pedro")

        # vou deletar para deixar o db vazio
        self.dao.delete(usuario)

        self.assertIsNone(result)

    def test_find_deve_retornar_none(self):
        """O usuário não existe no banco, por isso deve retornar None."""
        nome = "João"
        result = self.dao.find(nome=nome)

        self.assertIsNone(result)

    def test_delete_deve_retornar_none(self):
        """Depois de adicionado o usuário existe, então ele pode ser excluído."""
        entrada = Usuario(nome="Pedro", email="email", senha="1234")
        self.dao.add(entrada)

        usuario = self.dao.find("Pedro")
        result = self.dao.delete(usuario)

        self.assertIsNone(result)


if __name__ == '__main__':
    unittest.main()