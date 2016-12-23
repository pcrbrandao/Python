import unittest

from domain.usuario import Usuario
from utils import usuario_dao


class TestUserController(unittest.TestCase):
    """Os testes ainda não consideram todas as situações. Em desenvolvimento!"""

    def test_add_deve_retornar_none(self):
        """Acrescenta um usuário. Se não retornar erro está ok."""

        us = Usuario(nome='Pedro', email='email', senha='1234')
        result = usuario_dao.add(us)

        self.assertIsNone(result)

    def test_find_deve_encontrar(self):
        """Procura o usuario inserido no test_add"""

        nome = "Pedro"
        result = usuario_dao.find(nome=nome)
        print(result)

        self.assertEqual(result.nome, nome)

    def test_find_deve_retornar_none(self):
        """O usuário não existe no banco, por isso deve retornar None."""
        nome = "João"
        result = usuario_dao.find(nome=nome)

        self.assertIsNone(result)

if __name__ == '__main__':
    unittest.main()