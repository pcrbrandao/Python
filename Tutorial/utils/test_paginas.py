import unittest
from utils.usuario_dao import UsuarioDAO
from utils.paginas import Paginas


class TestUtils(unittest.TestCase):

    pag = Paginas()
    dao = UsuarioDAO()

    def test_total_de_paginas_deve_ser_um(self):
        """Se tem-se 10 registros e cada página tem 10, então tem-se 1 página"""
        registros = 10
        total = self.pag.total_de_paginas(registros, self.dao.usuarios_por_pagina)
        self.assertEqual(total, 1)

    def test_total_de_paginas_deve_ser_zero(self):
        """Se não há registros o número de páginas é zero"""
        registros = 0
        total = self.pag.total_de_paginas(registros, self.dao.usuarios_por_pagina)

        self.assertEqual(total, 0)

    def test_total_deve_ser_um_para_menor_que_dez(self):
        """Se registros é menor que dez e maior que zero o total é 1"""
        registros = 3
        total = self.pag.total_de_paginas(registros, self.dao.usuarios_por_pagina)

        self.assertEqual(total, 1)

    def test_total_deve_ser_dois_para_onze(self):
        registros = 11
        total = self.pag.total_de_paginas(registros, self.dao.usuarios_por_pagina)

        self.assertEqual(total, 2)

    def test_primeiro_registro_deve_ser_zero(self):
        pagina = 0
        primeiro = self.pag.primeiro_registro_da_pagina(pagina, self.dao.usuarios_por_pagina)

        self.assertEqual(primeiro, 0)

    def test_primeiro_registro_deve_ser_dez(self):
        pagina = 1
        primeiro = self.pag.primeiro_registro_da_pagina(pagina, self.dao.usuarios_por_pagina)

        self.assertEqual(primeiro, 10)

    def test_primeiro_registro_deve_ser_20(self):
        pagina = 2
        primeiro = self.pag.primeiro_registro_da_pagina(pagina, self.dao.usuarios_por_pagina)

        self.assertEqual(primeiro, 20)


if __name__ == '__main__':
    unittest.main()