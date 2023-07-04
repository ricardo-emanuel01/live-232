"""
Test Fixture:
    Preparação para testar alguma função, pode representar a criação de um
    banco de dados fake, diretórios ou até mesmo startar um server.

Test Case:
    É a unidade individual de teste. Checa as respostas dadas para um conjunto
    controlado de entradas.

Test Suite:
    Usada para agregar testes que devem ser executados em conjunto.

Test Runner:
    Componente que controla a execução dos testes e geram uma saída inteligível
    ao usuário, ele pode usar uma interface gráfica, textual ou retornar algum
    valor que signifique algo para o usuário, como 'OK' para dizer que todos
    os testes passaram, por exemplo.
"""
import unittest


class TestStringMethods(unittest.TestCase):

    def test_upper(self):
        self.assertEqual('foo'.upper(), 'FOO')

    def test_isupper(self):
        self.assertTrue('FOO'.isupper())
        self.assertFalse('Foo'.isupper())

    def test_split(self):
        s = 'hello world'
        self.assertEqual(s.split(), ['hello', 'world'])
        # check that s.split fails when the separator is not a string
        with self.assertRaises(TypeError):
            s.split(2)

if __name__ == '__main__':
    unittest.main()
