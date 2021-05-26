# test
import unittest
import SegClases

class test_result(unittest.TestCase): 
    def test_result(self):
        g = Gato()
        sonido = ""
        print(g.ronronear())
        print(g.maullar())
        print(g.gruñir())
        self.assertTrue(g.vivo())
