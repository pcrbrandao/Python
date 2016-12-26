import unittest

from domain.usuario import Usuario
from utils.usuario_dao import UsuarioDAO
from utils.random_strings import RandomStrings


class TestUserDAO(unittest.TestCase):
    """Os testes ainda não consideram todas as situações. Em desenvolvimento!"""

    dao = UsuarioDAO()
    rs = RandomStrings()

    def inserir_registros_para_teste(self, n=10):
        """Adicionar registros para teste.
        Criar listas nome, email e senha de comprimento n com strings aleatórias de comprimento 5,
        e inserir cada registro no db"""
        nomes = self.rs.lista_de_strings(comprimento=n)
        emails = self.rs.lista_de_strings(comprimento=n)
        senhas = self.rs.lista_de_strings(comprimento=n)

        for i in range(n):
            usuario = Usuario(nome=nomes[i], email=emails[i], senha=senhas[i])
            try:
                self.dao.add(usuario)
            except Exception as err:
                print("não pude adicionar o usuário {}. Erro: {}".format(usuario,err))
                return

    def test_delete_all(self):
        """Insere, lista e deleta tudo. Depois verifica se tem algum registro"""

        self.inserir_registros_para_teste()
        lista = self.dao.list()     # obtém a lista somente da primeira página
        for i in lista:             # agora imprime
            print(i)

        self.dao.delete_all()       # deleta tudo
        lista = self.dao.list()     # atualiza lista

        self.assertIsNone(lista)    # A lista vazia é None

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