import unittest

from app1 import conversaoC_F, conversaoF_C


class TestConverteF_C(unittest.TestCase):
    def test_iteracoes(self):
        valores = [(32, 0), (-40, -40), (50, 10)]
        for input_, output in valores:
            with self.subTest(input_=input_, output=output):
                conversaoF_C(input_) == output

    def test_converteF_C_deve_retornar_0_quando_receber_32(self):
        self.assertEqual(conversaoF_C(32), 0)

    def test_converteF_C_deve_retornar__40_quando_receber__40(self):
        self.assertEqual(conversaoF_C(-40), -40)

    def test_converteF_C_deve_retornar_10_quando_receber_50(self):
        self.assertEqual(conversaoF_C(50), 10)


class TestConverteC_F(unittest.TestCase):
    def test_converteC_F_deve_retornar_32_quando_receber_0(self):
        self.assertEqual(conversaoC_F(0), 32)

    def test_converteC_F_deve_retornar__40_quando_receber__40(self):
        self.assertEqual(conversaoC_F(-40), -40)

    def test_converteC_F_deve_retornar_50_quando_receber_10(self):
        self.assertEqual(conversaoC_F(10), 50)
