import unittest
import sys


# Pulando testes e falhas esperadas
class MyTestCase(unittest.TestCase):

    @unittest.skip('demonstrando skip')
    def test_nothing(self):
        self.fail("shouldn't happen")

    @unittest.skipIf(mylib.__version__ < (1, 3),
                     'not supported in this library version')
    def test_format(self):
        # Teste que funciona a partir de uma versão específica de uma biblioteca
        pass

    @unittest.skipUnless(sys.platform.startwith('win'), 'requires windows')
    def test_windows_support(self):
        # Código de teste específico para windows
        pass

    def test_maybe_skipped(self):
        if not external_resource_available():
            self.skipTest('external resource not availabe')
        # Código de teste que depende de um recurso externo
        pass
