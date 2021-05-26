# test
import unittest

class test_result(unittest.TestCase): 
    def test_result(self):
        class Animal(object):
            def __init__(self):
                vivo = True
    
        class Gato(Animal):
            def ronronear(self):
                sonido = "rrrrr"
                return sonido
            def maullar(self):
                sonido = "miauuuu"
                return sonido
            def gruñir(self):
                sonido = "grrrrr"
                return sonido
        g = Gato()
        sonido = ""
        print(g.ronronear())
        print(g.maullar())
        print(g.gruñir())
        self.assertTrue(g.vivo())
