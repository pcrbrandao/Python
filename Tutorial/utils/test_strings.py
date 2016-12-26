import unittest
from utils.random_strings import RandomStrings


class TestStrings(unittest.TestCase):
    """Teste para a classe Strings"""

    rs = RandomStrings()

    def test_string_aleatoria_deve_ter_comp_5(self):
        """O comprimento padrão deve ser 5"""
        texto = self.rs.string_aleatoria()
        print("O texto com 5 caracteres é: {}".format(texto))

        self.assertEqual(len(texto), 5)

    def test_string_aleatoria_deve_ter_comp_10(self):
        """O comprimento deve ser 10"""
        texto = self.rs.string_aleatoria(comprimento=10)
        print("O texto com 10 caracteres é: {}".format(texto))

        self.assertEqual(len(texto), 10)

    def test_lista_de_strings_deve_ter_comp_10(self):
        """A lista deve ser 10 itens"""
        lista = self.rs.lista_de_strings()

        print("A lista é:")
        for item in lista:
            print(item, end=' ')

        self.assertEqual(len(lista), 10)

