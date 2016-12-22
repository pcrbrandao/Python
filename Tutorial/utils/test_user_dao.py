import unittest

from domain.usuario import Usuario
from utils import usuario_dao


class TestUserController(unittest.TestCase):

    def test_add(self):

        us = Usuario(nome='Pedro', email='email', senha='1234')
        result = usuario_dao.add(us)

        self.assertIsNone(result)

if __name__ == '__main__':
    unittest.main()