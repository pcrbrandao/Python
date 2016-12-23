import unittest

from domain.usuario import Usuario
from utils import usuario_dao


class TestUserController(unittest.TestCase):
    """Os testes ainda não consideram todas as situações. Em desenvolvimento!"""

    def test_add_deve_retornar_none(self):
        """Acrescenta um usuário. Se não retornar erro está ok."""

        usuario = Usuario(nome='Pedro', email='email', senha='1234')
        result = usuario_dao.add(usuario)

        # o usuário deve ser encontrado no db
        usuario_db = usuario_dao.find("Pedro")
        print("o usuário {} foi adicionado com sucesso!".format(usuario_db))

        # vou deletar para deixar o db vazio
        usuario_dao.delete(usuario)

        self.assertIsNone(result)

    def test_find_deve_retornar_none(self):
        """O usuário não existe no banco, por isso deve retornar None."""
        nome = "João"
        result = usuario_dao.find(nome=nome)

        self.assertIsNone(result)

    def test_delete_deve_retornar_none(self):
        """Depois de adicionado o usuário existe, então ele pode ser excluído."""
        entrada = Usuario(nome="Pedro", email="email", senha="1234")
        usuario_dao.add(entrada)

        usuario = usuario_dao.find("Pedro")
        result = usuario_dao.delete(usuario)

        self.assertIsNone(result)

    def test_total_de_paginas_deve_ser_um(self):
        """Se tem-se 10 registros e cada página tem 10, então tem-se 1 página"""
        registros = 10
        total = usuario_dao.total_de_paginas(registros, usuario_dao.usuarios_por_pagina())

        self.assertEqual(total, 1)

    def test_total_de_paginas_deve_ser_zero(self):
        """Se não há registros o número de páginas é zero"""
        registros = 0
        total = usuario_dao.total_de_paginas(registros, usuario_dao.usuarios_por_pagina())

        self.assertEqual(total, 0)

    def test_total_deve_ser_um_para_menor_que_dez(self):
        """Se registros é menor que dez e maior que zero o total é 1"""
        registros = 3
        total = usuario_dao.total_de_paginas(registros, usuario_dao.usuarios_por_pagina())

        self.assertEqual(total, 1)

    def test_total_deve_ser_dois_para_onze(self):
        registros = 11
        total = usuario_dao.total_de_paginas(registros, usuario_dao.usuarios_por_pagina())

        self.assertEqual(total, 2)

if __name__ == '__main__':
    unittest.main()