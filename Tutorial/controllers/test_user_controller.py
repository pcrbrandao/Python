import unittest
from domain.usuario import Usuario
from controllers import usuario_controller


class TestUserController(unittest.TestCase):

    def test_add(self):

        us = Usuario(nome='Pedro', email='email', senha='1234')
        result = usuario_controller.add(us)

        self.assertIsNone(result)

if __name__ == '__main__':
    unittest.main()