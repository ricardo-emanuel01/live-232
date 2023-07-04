import unittest

"""
Supondo que quiséssemos testar um widget, poderíamos fazê-lo dessa
forma utilizando setUp() e tearDown()

Se setUp() for executado sem erro, tearDown() rodará independente
de haver falhas nos testes ou não.
"""

class WidgetTestCase(unittest.TestCase):
    def setUp(self):
        widget = Widget('The widget')

    def test_default_widget_size(self):
        self.assertEqual(self.widget.size(), (50, 50),
                         'incorrect default size')
        
    def test_widget_resize(self):
        self.widget.resize(100,150)
        self.assertEqual(self.widget.size(), (100,150),
                         'wrong size after resize')
        
    def tearDown(self):
        self.widget.dispose()


# Criando a própria suite
def suite():
    suite = unittest.TestSuite()
    suite.addTest(WidgetTestCase('test_default_widget_size'))
    suite.addTest(WidgetTestCase('test_widget_resize'))

if __name__ == '__main__':
    runner = unittest.TextTestRunner()
    runner.run(suite())
