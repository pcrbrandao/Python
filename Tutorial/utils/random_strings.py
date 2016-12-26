import random
import string
from utils.singleton import Singleton


class RandomStrings(Singleton):
    """Contém funções para manipulação de strings"""

    def __init__(self):
        Singleton.__init__(self)

    def string_aleatoria(self, comprimento=5, lista=string.ascii_letters + string.digits) -> str:
        """Retorna uma string de comprimento c escolhidos de uma lista"""
        return ''.join(random.choice(lista) for _ in range(comprimento))

    def lista_de_strings(self, comprimento=10, string_comprimento=5) ->[]:
        """Retorna uma lista de strings aleatórias"""
        return [self.string_aleatoria(comprimento=string_comprimento) for _ in range(comprimento)]