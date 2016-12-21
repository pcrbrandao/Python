import unittest
from domain.usuario import Usuario


class TestUsuario(unittest.TestCase):

    def test_contrutor_deve_funcionar(self):
        u = Usuario(
            nome="Pedro", email="pcrbrandao@hotmail.com", senha="1234")
        self.assertEqual(u.nome, "Pedro")
        self.assertEqual(u.senha, "1234")
        self.assertIsNone(u.id)